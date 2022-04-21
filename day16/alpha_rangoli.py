def print_rangoli(size):
    length = 4*n -3
    for x in range(n):
            d = 2*x + 1
            print('-'*((length-d)//2) + chr(96+n-x)*d + '-'*((length-d)//2))
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)