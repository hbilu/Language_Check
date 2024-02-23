import unittest
from unittest.mock import patch
from unittest.mock import Mock
import pandas as pd
from LanguageCheck import lang_error_check, langcheck

class TestLangDetect(unittest.TestCase):

    def setUp(self):
        """ Initializing a DataFrame for test set up."""
        self.mock_tweets = pd.DataFrame({'tweet': ['This is an English tweet.', 'Este es un tweet en Español']})
    
    # Temporarily replacing detect_langs function with a mock object. This object passes as an argument (mock_detect) to the test function.
    @patch('LanguageCheck.detect_langs')
    def test_lang_error_check(self, mock_detect):
        """ This test is for checking lang_error_check() which finds no error with given DataFrame. """
        # Setting a return value for mock object
        mock_detect.return_value = ['en']
        err_index = lang_error_check(self.mock_tweets)
        self.assertEqual(len(err_index), 0, "No error should be detected!")
        # to have mock object called at least one time to make sure the lang_detect is invoked as expected.
        mock_detect.assert_called()
    
    @patch('LanguageCheck.detect_langs')
    def test_langcheck(self, mock_detect):
        """
        This test checks followings:
        - Is there a language column in updated Dataframe after langcheck?
        - Are the detected languages represented in language column correct?
        """
        # Setting up a side effect function which will return ['en'] for English and ['es'] for otherwise.
        mock_detect.side_effect = lambda x: ['en'] if "English" in x else ['es']
        updated_tweets = langcheck(self.mock_tweets)
        self.assertIn('language', updated_tweets.columns, "DataFrame should have a language column.")
        self.assertEqual(updated_tweets.iloc[0]["language"][:-1], "'en'", "First tweet is English.")
        self.assertEqual(updated_tweets.iloc[1]["language"][:-1], "'es'", "Second tweet is Spanish.")
        mock_detect.assert_called()

if __name__ == '__main__':
    # running test with verbosity value 2 to have more detailed result including the names of tests being run.
    unittest.main(verbosity=2)