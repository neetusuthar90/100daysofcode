holder = {"accounts": [ 
     {'account':100,'name': 'Neetu', 'balance':889.00},
     {'account':200, 'name':'Liptan','balance':1050.45}] }

import json
## JSON is just a big string of data
with open('accounts.json','w') as acc:
    json.dump(holder,acc)  #dumo is function take two variable

with open('accounts.json','r') as account:
    account_json = json.load(account) #account_json is a dictionaory

print(type(account_json)) 
print(account_json['accounts']) 
print(account_json['accounts'][0])

with open('accounts.json','r') as account:
    print(json.dumps(json.load(account), indent=4))




