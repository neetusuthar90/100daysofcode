# Basi dictionary Operation
roman = {'I':1, 'II':2,'III':3, 'V':7,'X':100}

print(roman['II']) #Value of II
roman['X'] = 10 #Change the value of key if it is not in dictionary then add it to dictionary
roman['L'] = 50
del roman['III'] #deleate a key
roman.pop('X') #will delete value of X
roman.get('V')
print(roman)
roman['v'] = 5 # v ia differnt from V so it will add

print(roman)
print(roman.get('III', 'Not in dictionary'))
print('V' in roman)
print('III' in roman)
print('III' not in roman)

print(list(roman.keys())) #Listing of object
print(list(roman.items()))
