from api import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_is_positive():
    from api.sentiment import is_positive

    assert is_positive("This is a positive sentence.")
    assert not is_positive("This is a negative sentence.")


def test_twitter_preprocess():
    from api.preprocess import twitter_preprocess

    assert twitter_preprocess("This is a tweet. #testing @martin") == "tweet testing"
    assert (
        twitter_preprocess("Check this link out https://www.google.com") == "check link"
    )


def test_make_predictions():
    from api.predict import make_predictions

    tweets = [
        "This is a tweet. #testing @martin",
        "fuck everyone who supports human rights",
        "what a bitch",
    ]
    predictions = make_predictions(tweets)
    assert predictions == [2, 0, 1]
