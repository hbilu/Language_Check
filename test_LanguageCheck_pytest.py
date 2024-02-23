import pytest
import pandas as pd
from LanguageCheck import lang_error_check, langcheck

@pytest.fixture
def mock_tweets():
    """ This function creates a DataFrame for testing."""
    data = {'tweet': ['This is an English tweet.', 'Este es un tweet en Español']}
    return pd.DataFrame(data)

def test_lang_error_check(mocker, mock_tweets):
    """ This test is for checking lang_error_check() which finds no error with given DataFrame. """
    # mocking detect_langs function and setting return value for it.
    mock_detect = mocker.patch('LanguageCheck.detect_langs', return_value=['en'])
    err_index = lang_error_check(mock_tweets)
    assert len(err_index) == 0
    # to have mock object called at least one time to make sure the lang_detect is invoked as expected.
    mock_detect.assert_called()

def test_langcheck(mocker, mock_tweets):
    """ This test checks followings:
        - Is there a language column in updated Dataframe after langcheck?
        - Are the detected languages represented in language column correct?
    """
    # mocking detect_langs function and setting a (side effect) function to be called with mock.
    mock_detect = mocker.patch('LanguageCheck.detect_langs', side_effect=lambda x: ['en'] if "English" in x else ['es'])
    updated_tweets = langcheck(mock_tweets)
    assert "language" in updated_tweets.columns
    assert updated_tweets.iloc[0]["language"][:-1] == "'en'"
    assert updated_tweets.iloc[1]["language"][:-1] == "'es'"
    mock_detect.assert_called()