
s = input()
print(any(k.isalnum() for k in s))
print(any(k.isalpha() for k in s))
print(any(k.isdigit() for k in s))
print(any(k.islower() for k in s))
print(any(k.isupper() for k in s))
