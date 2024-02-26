
from line_profiler import LineProfiler
import pandas as pd
from LanguageCheck import langcheck, lang_error_check
import sys

def main():
    tweets_df = pd.read_csv('tweets.csv', sep=';', index_col=0, chunksize=100)
    # print(tweets_df.shape)

    for i, chunk in enumerate(tweets_df):
        # detecting and printing tweets which gives a language error
        err_index = lang_error_check(chunk)

        # removing tweets with language error
        chunk.drop(chunk.index[err_index], inplace=True)
        # print(tweets_df.shape)

        # language checking
        chunk = langcheck(chunk)

        # count the occurrences of languages and store them in newly created DataFrame, count_lang
        count_lang = pd.DataFrame(chunk.groupby('language').text.count().sort_values(ascending=False))
        print(count_lang)

        if i==0:
            chunk.to_csv('tweets_langcheck.csv', mode='w', index=False)
        else:
            chunk.to_csv('tweets_langcheck.csv', mode='a', index=False, header=False)

    # line profiling for langcheck function
    lp = LineProfiler()
    lp_wrapper = lp(langcheck)
    lp_wrapper(chunk)
    lp.print_stats()

if __name__ == '__main__':
    sys.exit(main())  