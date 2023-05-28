
from langdetect import detect_langs


def lang_error_check(tweets):
    """
    The function checks whether there is a syntax/symbol that gives error for language check with langdetect.
        Parameters:
             tweets (DataFrame): Dataframe which covers the data to be checked
        Returns:
             error_index (list): A list of indexes which giving an error
    """
    # creation of an empty list for tweets which gives a language error
    error_index = []
    # language check with detect_langs
    # The tweets giving errors will be printed and their indexes are stored in a list.
    for index in range(0, len(tweets), 1):
        try:
            detect_langs(tweets.iloc[index, 0])
        except Exception:
            language = "error"
            print("This row throws an error:", tweets.iloc[index, 0])
            error_index.append(index)
    return error_index


def langcheck(tweets):
    """
    The function implies language check
        Parameters:
            tweets (DataFrame): Dataframe which stores the data to be checked
        Returns:
            tweets (DataFrame): Enriched DataFrame with a language column, the result of the language check function.
    """
    # creation of an empty list for language results
    lang = []
    # detecting languages with their probabilities
    for index in range(0, len(tweets), 1):
        lang.append(detect_langs(tweets.iloc[index, 0]))
    # using list comprehension to extract abbreviations of language which has the highest probability
    lang = [str(lang1).split(':')[0][1:] for lang1 in lang]
    # add languages with language column to the tweets_df DataFrame
    tweets['language'] = lang
    return tweets
