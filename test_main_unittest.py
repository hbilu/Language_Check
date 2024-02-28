import unittest
from unittest.mock import patch
import os
from main import main

class TestProcess(unittest.TestCase):
    # setup test environment
    def setUp(self):
        self.input_file = 'tweets.csv'
        self.output_file = 'tweets_langcheck.csv'
        with open(self.input_file, 'w') as f:
            f.write("18; you guys didn`t say hi or answer my questions yesterday  but nice songs.;positive")
            f.write("25; thats so cool;positive")
            f.write("20;Stupid storm. No river for us tonight;negative")
            f.write("49;Not happy;negative")
            f.write("920; 6 am.  you?;neutral")
    
    @patch('main.lang_error_check')
    @patch('main.langcheck')
    def test_process(self, mock_langcheck, mock_lang_error_check): 
        # mocking lang_error_check to return an empty list
        mock_lang_error_check.return_value = []
        # mocking langcheck to add a 'language' column to the DataFrame
        mock_langcheck.side_effect = lambda df: df.assign(language='en')
        main()
        # checking output file is created or not
        self.assertTrue(os.path.exists(self.output_file),"Output file was not created")
        # checking output file is empty or not
        self.assertTrue(os.path.getsize(self.output_file) > 0, "Output file is empty")

    # teardown of the test files
    def tearDown(self):
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

if __name__=='__main__':
    unittest.main(verbosity=2)