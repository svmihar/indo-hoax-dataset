from ehe_hoaxer import pull_paragraph_hoax
import pandas as pd
import os


links = open('hoax_new.txt', 'r').read().splitlines()

df = pd.DataFrame()


if __name__ == "__main__":
    for link in links:
        paragraf = pull_paragraph_hoax(link)
        df_ = pd.Series([link, paragraf])
        df__ = df.append(df_, ignore_index=True)
        if not os.path.exists('csv/'):
            os.makedirs('csv/')
        df__.to_csv('csv/eya.csv', mode='a', index=False)
