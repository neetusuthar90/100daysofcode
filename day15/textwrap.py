def wrap(string, max_width):
    list = [string[i:i+max_width]  for i in range(0, len(string), max_width)]
    string1 = '\n'.join(list)
    return string1


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)