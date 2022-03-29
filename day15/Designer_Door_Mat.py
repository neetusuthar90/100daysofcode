input = input().split()
N = int(input[0])
M = int(input[1])
puss = ".|."
for x in range(N//2):
    d = 2*x + 1
    tapri = M-d
    str = ('-' * ((tapri//2)-d)) + (puss * d) + ('-' * ((tapri//2)-d))
    print(str)
temp = (M-7)//2
print(('-' * temp) + 'WELCOME' + ('-' * temp))

for x in reversed(range(N//2)):
    d = 2*x + 1
    tapri = M-d
    str = ('-' * ((tapri//2)-d)) + (puss * d) + ('-' * ((tapri//2)-d))
    print(str)
