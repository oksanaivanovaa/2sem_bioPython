# Numpy , pandas

import pandas as pd

df = pd.read_csv("tb-raw.csv")
print(df)

df = pd.melt(df, id_vars=['country', 'year'], value_name='cases').dropna()
tmp_df = df['variable'].str.extract("(\D)(\d+)(\d{2})")


values = {0: 'm', 1: 65, 2: '+'}
tmp_df = tmp_df.fillna(value=values)


df['sex'] = tmp_df[0]
df = df.drop('variable', 1)


df['age'] = tmp_df[[1, 2]].apply(lambda x: '-'.join(x.map(str)), axis=1)
print(df)