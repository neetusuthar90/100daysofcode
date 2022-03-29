import re
def count_substring(string, sub_string): 
    c = 0
    d = len(sub_string)
    for i in range(0,len(string)):
        print(sub_string, string[i:i+d])
        if sub_string == string[i:i+d]: 
            c = c + 1
    return(c)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)