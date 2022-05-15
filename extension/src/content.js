import optionsStorage from "./options-storage.js";
import browser from "webextension-polyfill";

const tweets = new Set();
let id = 0;

const createWarning = (elID) => `
<div id="${elID}-warning" style="display: flex;background: rgb(22, 24, 28);padding: 1rem;border-radius: 16px;justify-content: space-between;">
  <div style="color: rgb(113, 118, 123);font-family: TwitterChirp, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Helvetica, Arial, sans-serif;">
    The following tweet was hidden by Uptone due to offensive content. </div>
  <div id="${elID}-btn" style="color: rgb(239, 243, 244);font-weight: 700;font-size: 15px;font-family: TwitterChirp, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Helvetica, Arial, sans-serif;">View</div>
</div>`;

let finished = true;
let options;

const predict = async (tweetData) => {
  return browser.runtime
    .sendMessage({
      method: "POST",
      action: "xhttp",
      url: "http://localhost:5000/predict",
      data: JSON.stringify({ tweets: tweetData }),
    })
    .then((message) => {
      return JSON.parse(message).predictions;
    });
};

const filterTweets = async () => {
  if (!finished) return;
  finished = false;
  // Get all tweets from page
  const _tweets = [...document.querySelectorAll("[data-testid='tweet']")];

  // Get all new tweets by set difference
  const newTweets = _tweets.filter((x) => !tweets.has(x));

  // Parse tweets
  const newTweetsText = [];
  for (const tweet of newTweets) {
    const textelement = tweet.querySelector("[data-testid=tweetText]");
    if (!textelement) {
      newTweetsText.push("");
      continue;
    }
    newTweetsText.push(textelement.firstChild.innerText);
  }
  if (!newTweetsText.length) {
    newTweets.forEach((tweet) => tweets.add(tweet));
    finished = true;
    return;
  }

  // Process tweets
  const predictions = await predict(newTweetsText);

  for (const idx in newTweets) {
    const tweet = newTweets[idx];
    const prediction = predictions[idx];
    if (prediction === 2) continue;
    if (!options.offensiveLanguage && prediction === 1) continue;
    if (!options.hateSpeech && prediction === 0) continue;
    const elID = `uptone-${id++}`;

    if (
      tweet.firstChild.firstChild.firstChild &&
      tweet.firstChild.firstChild.firstChild.childNodes[2] !== undefined
    ) {
      const contentArea = tweet.firstChild.firstChild.firstChild;
      contentArea.childNodes[2].style.display = "none";
      contentArea.childNodes[2].id = `${elID}-content`;
      contentArea.innerHTML += createWarning(elID);
    } else if (
      tweet.firstChild.firstChild.firstChild.childNodes[1].childNodes[1] &&
      tweet.firstChild.firstChild.firstChild.childNodes[1].childNodes[1]
        .childNodes[1] !== undefined
    ) {
      const contentArea =
        tweet.firstChild.firstChild.firstChild.childNodes[1].childNodes[1];
      contentArea.childNodes[1].style.display = "none";
      contentArea.childNodes[1].id = `${elID}-content`;
      contentArea.innerHTML += createWarning(elID);
    }
    const button = document.getElementById(`${elID}-btn`);
    if (button) {
      button.addEventListener("click", (event) => {
        event.stopPropagation();
        const currentID = event.currentTarget.id.split("-btn")[0];
        document.getElementById(`${currentID}-content`).style.display = "block";
        document.getElementById(`${currentID}-warning`).style.display = "none";
      });
    }
  }

  // Update tweets with the new tweets
  newTweets.forEach((tweet) => tweets.add(tweet));
  finished = true;
};

async function init() {
  options = await optionsStorage.getAll();
  await filterTweets();
}

init();

document.addEventListener("scroll", async () => {
  await filterTweets();
});
