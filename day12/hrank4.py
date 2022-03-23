from numpy import average


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for n,g in student_marks.items():
        if n == query_name:
            average = (sum(g))/len(g)
            print("{:.2f}".format(average))
        