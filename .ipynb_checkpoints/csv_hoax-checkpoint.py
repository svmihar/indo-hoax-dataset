from ehe_hoaxer import pull_paragraph_hoax

links = open('hoax.txt','r').read().splitlines()

for link in links: 
    paragraf = ambil(link)
    df_ =pd.Series([link, paragraf])
    df__ = df.append(df_, ignore_index=True)
    df__.to_csv('eya.csv',mode='a')
    
