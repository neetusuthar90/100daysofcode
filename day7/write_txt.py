"""Formation of txt file and write data into that file"""
from numpy import dtype


with open('accounts.txt', mode = 'w') as account:  
    account.write('100 Liptan 78.909\n')
    account.write('200 Neetu 60.89\n')
    account.write('300 Neha 45.3456\n')
    account.write('400 Yuv 59.32\n')
    account.write('500 Yes 100.50\n')
    account.write('600 Ginni 88.99\n')
