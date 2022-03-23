if __name__ == '__main__':
    N = int(input())
    List = []
    for i in range(N):
        st = input()
        op = st.rsplit(' ')[0]
        if op == 'append':
            a = int(st.rsplit(' ')[1])
            List.append(a)
        elif op == 'insert':
            a = int(st.rsplit(' ')[1])
            b = int(st.rsplit(' ')[2])
            List.insert(a, b)
        elif op == 'remove':
            a = int(st.rsplit(' ')[1])
            List.remove(a)
        elif op == 'sort':
            List.sort()
        elif op == 'pop':
            List.pop()
        elif op == 'reverse':
            List.reverse()
        elif op == 'print':
            print(List)
