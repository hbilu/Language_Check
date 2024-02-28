import pytest
import os
from main import main

@pytest.fixture
def setup():
    # setup test environment
    input_file = 'tweets.csv'
    output_file = 'tweets_langcheck.csv'
    with open(input_file, 'w') as f:
        f.write("18; you guys didn`t say hi or answer my questions yesterday  but nice songs.;positive")
        f.write("25; thats so cool;positive")
        f.write("20;Stupid storm. No river for us tonight;negative")
        f.write("49;Not happy;negative")
        f.write("920; 6 am.  you?;neutral")
    yield input_file, output_file
    
    # teardown of the test files
    if os.path.exists(input_file):
        os.remove(input_file)
    if os.path.exists(output_file):
        os.remove(output_file)

def test_process(mocker, setup):
    # mocking lang_error_check to return an empty list
    mocker.patch('main.lang_error_check', return_value=[])

    # mocking langcheck to add a 'language' column to the DataFrame
    mocker.patch('main.langcheck', side_effect = lambda df: df.assign(language='en'))

    input_file, output_file = setup
    main()
    # checking output file is created or not
    assert os.path.exists(output_file), "Output file was not created"
    # checking output file is empty or not
    assert os.path.getsize(output_file) > 0, "Output file is empty"

