
import pandas as pd
from langdetect import detect_langs

tweets_df = pd.read_csv('tweets.csv', sep=';', index_col=0)
# print(tweets_df.head())
# print(tweets_df.shape)

# creation of an empty list for tweets which gives a language error
error_index = []

# language check with detect_langs
# if there is a tweet which gives an error by detect_langs, this tweet will be printed.
for index in range(0, len(tweets_df['text']), 1):
    try:
        detect_langs(tweets_df.iloc[index, 0])
    except Exception:
        language = "error"
        print("This row throws an error:", tweets_df.iloc[index, 0])
        error_index.append(index)

# removing tweets with language error
tweets_df.drop(tweets_df.index[error_index], inplace=True)
# print(tweets_df.shape)

# creation of an empty list for language results
lang = []

# detecting languages with their probabilities
for index in range(0, len(tweets_df['text']), 1):
    lang.append(detect_langs(tweets_df.iloc[index, 0]))
# print(lang)

# using list comprehension to extract abbreviations of language which has the highest probability
lang = [str(lang1).split(':')[0][1:] for lang1 in lang]

# add languages with language column to the tweets_df DataFrame
tweets_df['language'] = lang
print(tweets_df.head())

# count the occurrences of languages and store them in newly created DataFrame, count_lang
count_lang = pd.DataFrame(tweets_df.groupby('language').text.count().sort_values(ascending=False))

print(count_lang)
