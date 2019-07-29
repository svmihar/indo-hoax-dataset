from pengambil_hoax import ambil
import pandas as pd 

links = open('hoax_new.txt','r').read().splitlines()

df = pd.DataFrame()

for link in links: 
    paragraf = ambil(link)
    df_ =pd.Series([link, paragraf])
    df__ = df.append(df_, ignore_index=True)
    df__.to_csv('eya.csv',mode='a')
    
