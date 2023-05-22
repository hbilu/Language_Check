
from langdetect import detect_langs

def langcheck(tweets):
    # creation of an empty list for tweets which gives a language error
    error_index = []
    # language check with detect_langs
    # if there is a tweet which gives an error by detect_langs, this tweet will be printed.
    for index in range(0, len(tweets), 1):
        try:
            detect_langs(tweets.iloc[index, 0])
        except Exception:
            language = "error"
            print("This row throws an error:", tweets.iloc[index, 0])
            error_index.append(index)
    # removing tweets with language error
    tweets.drop(tweets.index[error_index], inplace=True)
    # print(tweets.shape)
    # creation of an empty list for language results
    lang = []
    # detecting languages with their probabilities
    for index in range(0, len(tweets), 1):
        lang.append(detect_langs(tweets.iloc[index, 0]))
    # print(lang)
    # using list comprehension to extract abbreviations of language which has the highest probability
    lang = [str(lang1).split(':')[0][1:] for lang1 in lang]
    # add languages with language column to the tweets_df DataFrame
    tweets['language'] = lang
    return tweets

