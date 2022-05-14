import re
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer
import demoji
import contractions
import string

tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

abbreviations = {
    "lol": "laughing",
    "lmao": "laughing",
    "lmfao": "laughing",
    "kys": "kill yourself",
    "stfu": "shut up",
    "lmk": "let me know",
    "nvm": "nevermind",
    "tbh": "to be honest",
    "bc": "because",
    "cuz": "because",
    "btw": "by the way",
    "cya": "see you",
    "imho": "in my humble opinion",
    "imo": "in my opinion",
    "ftw": "for the win",
    "fyi": "for your information",
    "gtg": "got to go",
    "gr8": "great",
    "ily": "i love you",
    "fs": "for sure",
    "jk": "just kidding",
    "ong": "for real",
    "fr": "for real",
    "thx": "thanks",
    "omg": "oh my god",
    "ttyl": "talk to you later",
}


def twitter_preprocess(text: str):
    """
    Preprocessor for tweets
    Remove punctuation
    Remove hashtags
    Remove stopwords
    Remove URLs, hashtags, and usernames
    Expand common abbreviations and contractions
    Convert emojis to words
    Convert to lowercase
    Remove non-ASCII characters
    Stem words
    """
    tokens = tweet_tokenizer.tokenize(text)
    filtered_tokens = []
    for token in tokens:
        # Remove punctuation
        if token in string.punctuation:
            continue
        # Remove hashtags
        if token.startswith('#'):
            token = token[1:]
        # Remove stopwords
        if token in stop_words:
            continue
        # Remove urls
        if token.startswith('http'):
            continue
        # Expand common abbreviations and contractions
        token = contractions.fix(token)
        for key, value in abbreviations.items():
            token = re.sub(r'\b' + key + r'\b', value, token)
        # Convert emojis to words
        token = demoji.replace_with_desc(token, '')
        # Remove non-ASCII characters
        token = re.sub(r'[^\x00-\x7F]+', '', token)
        # Lemmatize
        token = lemmatizer.lemmatize(token)
        if token != '':
            filtered_tokens.append(token)
    text = " ".join(filtered_tokens)
    return text