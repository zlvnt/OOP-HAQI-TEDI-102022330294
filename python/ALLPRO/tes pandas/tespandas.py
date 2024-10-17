import pandas as pd

data = pd.read_csv('kapal_titanic.csv')
print(data.head())

data.to_excel('dataexcel.xlsx', index=False, sheet_name = 'boy')