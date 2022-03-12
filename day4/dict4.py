grade_book = { 
    'Liptan': [67,98,78,55],
    'Neetu': [65,78,90,45],
    'Latika': [69,99,85,88],
    'Diva': [89,98,97,95]
}

grades_total = 0
grades_count = 0

for name,grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades)}')
    grades_total += total
    grades_count += len(grades)

print(f'Class average is:{grades_total/grades_count}')

