try:
    print('try suite with no exception raised.')
except:
    print('this will not execute')
else:
    print('else execute because no exception in try suite')
finally:
    print('finally always executes')

try:
    print('try suite with no exception raised.')
    int('hello')
    print('this will not execute')
except ValueError:
    print('a valueerror occured')
else:
    print('else execute because no exception in try suite')
finally:
    print('finally always executes')