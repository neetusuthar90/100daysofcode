def dec_bin(X):
    """ Decimal to binary conversion """
    s = ''
    while X >= 1:
        qutioent = X//2
        remainder = X % 2
        s = s + str(remainder)
        X = qutioent
    return(s[::-1])


def bin_dec(num):
    """ Binary to Decimal """
    n = len(str(num))
    bin = 0
    bin_list = [int(d) for d in str(num)]
    for i in range(n):
        bin = bin + bin_list[i] * pow(2, (n-i-1))
    return(bin)


menu = int(
    input("Choose an option:\n 1. Decimal to binary. \n 2. Binary to decimal. \n"))
if menu == 1:
    value = int(input('Enter a decimal number: '))
    print(dec_bin(value))
elif menu == 2:
    num = int(input('Enter binary number: '))
    print(bin_dec(num))
