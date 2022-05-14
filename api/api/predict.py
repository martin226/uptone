from api.consts import HATE_SPEECH, OFFENSIVE, NEITHER
from api.preprocess import twitter_preprocess
from api.sentiment import is_positive
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
import pickle
import os
import sys

# Change to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load model and tokenizer
if not os.path.exists('./bin/tokenizer.pickle'):
    print('Tokenizer not found')
    sys.exit(1)
if not os.path.exists('./bin/hatespeech.bin'):
    print('Model not found')
    sys.exit(1)

with open('./bin/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
model = load_model('./bin/hatespeech.bin')


def make_predictions(tweets: list) -> list:
    """
    Returns the predicted classes of the tweets.
    :param tweets: list of tweets
    :return: list of predicted classes
    """
    predictions = [None] * len(tweets)

    # Preprocess tweets
    tweets = [twitter_preprocess(tweet) for tweet in tweets]

    # Handle false positives
    for i in range(len(tweets)):
        if is_positive(tweets[i]):
            predictions[i] = NEITHER

    # Tokenize text
    tokens = tokenizer.texts_to_sequences(tweets)
    # Pad tokens
    tokens = sequence.pad_sequences(tokens, maxlen=100)

    # Make prediction
    p = model.predict(tokens)
    for i in range(len(p)):
        if predictions[i] == NEITHER:
            continue
        if p[i][0] > 0.5:
            predictions[i] = HATE_SPEECH
        elif p[i][1] > 0.5:
            predictions[i] = OFFENSIVE
        else:
            predictions[i] = NEITHER
    return predictions
