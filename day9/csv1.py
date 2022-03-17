import csv
with open('data.csv', mode='w', newline='') as d:
    writer = csv.writer(d)
    writer.writerow([100, 'Liptan', 78.909])
    writer.writerow([200, 'Neetu', 60.89])
    writer.writerow([300, 'Yuv', 59.32])

with open('data.csv', 'r', newline='') as account:
    print(f'{"Account": <10} {"Name":<10} {"Balance":>10}')
    reader = csv.reader(account)
    for r in reader:
        account, name, balance = r
        print(f'{account:<10}{name:<10}{balance:>10}')
