""" Read file accounts.txt and display the data"""
with open('accounts.txt',mode = 'r') as accounts:
    print(f'{"Account" :<10} {"Name":<10} {"Balance" :>10}') #f string 
    for rec in accounts:
        account, name, balance = rec.split()
        print(f'{account:<10}{name:<10}{balance:>10}')

""" Create a tempororay file from accounts.txt"""
accounts = open('accounts.txt',mode = 'r')
temp_file = open('temp_file.txt',mode = 'w')
with accounts, temp_file:
    for record in accounts:
        account,name,balance = record.split()
        if int(account) != 300:
            temp_file.write(record)
        else:
            new_record = ' '.join([account, 'William', balance])
            temp_file.write(new_record + '\n')

""" Remove accounts.txt and change temorary file as accounts.txt"""
import os
#os.remove('accounts.txt')
os.rename('temp_file.txt','accounts.txt')