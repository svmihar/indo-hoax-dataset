import pandas as pd 

df = pd.read_csv(r'data/600 news with valid hoax label.csv')

df = pd.read_excel(r'data/600 news labelling process.xlsx')

print(df.head())