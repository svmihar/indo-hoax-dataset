import pandas as pd 
from pengambil_hoax import ambil
import os 
df = pd.DataFrame()
links = open('hoax.txt','r').read().splitlines()

for i, link in enumerate(links): 

#     print(f'{link}')
#     print(i)
    paragraf = ambil(link)
    df_ =pd.Series([link, paragraf])
    df__ = df.append(df_, ignore_index=True)
    df__.to_csv('eya.csv',mode='a', header=False)

os.system('python3 pusher.py')