# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
value = []
for i in range(T):
    value.append(list(input().split()))
for a, b in value:
    try:
        a = int(a)
        b = int(b)
        res = a/b
    except ZeroDivisionError as ex:
        print('Error Code:',ex)
    except ValueError as ex:
        print('Error Code:',ex)
    else:
        print(res)
