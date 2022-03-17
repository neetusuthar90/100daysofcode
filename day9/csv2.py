import pandas as pd

## name = [] we have to mention because in our data.csv we have not given the headlines \\ 
# .....if we skip this than it will choose first line of csv as heading
##df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv',names  = ['Accounts','Name','Balance'])
print(df)
df.to_csv('from_dataframe.csv', index= False)
