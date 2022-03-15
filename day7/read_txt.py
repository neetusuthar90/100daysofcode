with open('accounts.txt',mode = 'r') as accounts:
    print(f'{"Account" :<10} {"Name":<10} {"Balance" :>10}') #f string 
    for rec in accounts:
        account, name, balance = rec.split()
        print(f'{account:<10} {name:<10} {balance:>10}')

        



