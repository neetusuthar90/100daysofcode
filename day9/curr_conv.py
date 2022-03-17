import requests 
import json
response = requests.get("http://api.exchangeratesapi.io/v1/latest?" +
       "access_key=df2cdbb5e89eb6ba2a5dbecd57869c6d")
currency = response.json()
with open('currency.json', 'w') as f:
    json.dump(currency, f)

with open('currency.json','r') as curr:
    curr_json = json.load(curr)
    temp = curr_json['rates']
    print(temp['USD'])
        


