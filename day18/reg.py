import re

T = int(input())
for i in range(T):
    key = input()
    try:
        re.compile(key)
        valid = True
    except re.error:
        valid = False
    print(valid)
