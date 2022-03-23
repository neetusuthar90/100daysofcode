from collections import deque

N = int(input())
d = deque()
for i in range(N):
    st = input()
    a = st.rsplit(' ', 1)[0]
    if a == 'append':
        b = st.rsplit(' ', 1)[1]
        d.append(b)
    elif a == 'appendleft':
        b = st.rsplit(' ', 1)[1]
        d.appendleft(b)
    elif a == 'pop':
        d.pop()
    elif a == 'popleft':
        d.popleft()

print(*d)
