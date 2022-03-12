country_codes = {'India': 'in', 'Finland': 'fi','United states': 'usa'}
country_codes['Nepal'] = 'np' #Add new item
#print(country_codes)
#print(len(country_codes))
first_item = list(country_codes.items())[0][0]
print(first_item)
if country_codes:
    print('Dict is not empty')
else:
    print('Dict is empty')

"""for removing items in dictionary"""
country_codes.clear()
if country_codes:
    print('Dict is not empty')
else:
    print('Dict is empty')