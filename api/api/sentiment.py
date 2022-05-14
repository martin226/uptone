from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def is_positive(text: str) -> bool:
    """
    Returns True if the text is positive, False otherwise.
    """
    return sia.polarity_scores(text)["compound"] > 0
