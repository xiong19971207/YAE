import pandas as pd


a = pd.read_csv('test.csv',encoding='utf-8')

print(a.columns)


print(a.dtypes)