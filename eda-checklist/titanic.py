import pandas as pd

df = pd.read_csv("titanic.csv")

df.head()
df.shape
df.columns

df.info()
df.isnull().sum()

