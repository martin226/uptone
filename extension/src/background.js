import "./options-storage.js";
import browser from "webextension-polyfill";

browser.runtime.onMessage.addListener((request, sender, callback) => {
  if (request.action == "xhttp") {
    let xhttp = new XMLHttpRequest();
    let method = request.method ? request.method.toUpperCase() : "GET";

    xhttp.onload = function () {
      callback(xhttp.responseText);
    };
    xhttp.onerror = function () {
      // Do whatever you want on error. Don't forget to invoke the
      // callback to clean up the communication port.
      callback();
    };
    xhttp.open(method, request.url, true);
    if (method == "POST") {
      xhttp.setRequestHeader("Content-Type", "application/json");
    }
    xhttp.send(request.data);
    return true; // prevents the callback from being called too early on return
  }
});
