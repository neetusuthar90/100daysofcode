days_per_month = {'January': 31, 'Feburary': 28, 'March': 31, 'April': 30}
print(days_per_month)
# items() for all the entries
for month,day in days_per_month.items():
    #print(f'{month} has {day} days.' )
    print(month,day)
#Another way
days_view = days_per_month.items()
for month,day in days_view:
    print('%s month has %d days!'%(month,day))

# keys() and value() for keys and values respectively
for month in days_per_month.keys():
    print(month)
    
for day in days_per_month.values():
    print(day)

#Sorting keys alphabetically and values in increasing order
sort = sorted(days_per_month.keys())
for m in sort:
    print(m)
so = sorted(days_per_month.values())
for day in so:
    print(day)