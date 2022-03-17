import requests 
import json
response = requests.get("http://api.exchangeratesapi.io/v1/latest?" +
       "access_key=df2cdbb5e89eb6ba2a5dbecd57869c6d")
currency = response.json()
currency1 = input('Enter the input currency code: ') ## Value of 1 EUR
currency2 = input('Enter the output currency code: ')
A = currency['rates'][currency1]
B = currency['rates'][currency2]
amount = int(input('Amount you want to convert from currency1 to currency2: '))
amount_in_euro=amount/A
print(amount_in_euro*B)




