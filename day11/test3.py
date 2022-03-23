n = int(input())
words_counter = {}

for i in range(n):
    a = input()
    if a in words_counter:
        words_counter[a] = words_counter[a] + 1
    else:
        words_counter[a] = 1

#print(words_counter)
print(len(words_counter))
print(' '.join(map(str, words_counter.values())))