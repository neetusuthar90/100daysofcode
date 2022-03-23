A = []
B = []
N = int(input())
for _ in range(N):
    name = input()
    score = float(input())
    A.append([name, score])
    B.append(score)


A.sort()
grade = list(set(B))
grade.sort()
second_lwst = grade[1]
for i in A:
    if i[1] == second_lwst:
        print(i[0])
