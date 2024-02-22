import pytest
import pandas as pd
from LanguageCheck import lang_error_check, langcheck

@pytest.fixture
def mock_tweets():
    data = {'tweet': ['This is an English tweet.', 'Este es un tweet en Español']}
    return pd.DataFrame(data)

def test_lang_error_check(mocker, mock_tweets):
    mock_detect = mocker.patch('LanguageCheck.detect_langs', return_value=["en"])
    err_index = lang_error_check(mock_tweets)
    assert len(err_index) == 0
    mock_detect.assert_called()

def test_langcheck(mocker, mock_tweets):
    mocker.patch('LanguageCheck.detect_langs', side_effect=lambda x: ["en"] if "English" in x else ["es"])
    updated_tweets = langcheck(mock_tweets)
    assert "language" in updated_tweets.columns
    assert updated_tweets.iloc[0]["language"][:-1] == "'en'"
    assert updated_tweets.iloc[1]["language"][:-1] == "'es'"