def average(array):
    # your code goes here
    st = set(map(int, array))
    av = (sum(st))/len(st)
    return("{:.3f}".format(av))
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)