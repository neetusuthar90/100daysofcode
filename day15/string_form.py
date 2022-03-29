def print_formatted(number):
    # your code goes here
    w = len("{0:b}".format(number))
    for k in range(1,n+1):
        de = str(k)
        oc = (oct(k))[2:]
        he = (hex(k).upper())[2:]
        bi = (bin(k))[2:]
        print(de.rjust(w), oc.rjust(w), he.rjust(w), bi.rjust(w))
        # print ("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(k, width=w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)