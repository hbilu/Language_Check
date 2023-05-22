
from line_profiler import LineProfiler
import pandas as pd
from LanguageCheck import langcheck

tweets_df = pd.read_csv('tweets.csv', sep=';', index_col=0)
# print(tweets_df.head())
# print(tweets_df.shape)

tweets_df = langcheck(tweets_df)

# count the occurrences of languages and store them in newly created DataFrame, count_lang
count_lang = pd.DataFrame(tweets_df.groupby('language').text.count().sort_values(ascending=False))
print(count_lang)

lp = LineProfiler()
lp_wrapper = lp(langcheck)
lp_wrapper(tweets_df)
lp.print_stats()
