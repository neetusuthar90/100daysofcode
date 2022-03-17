grades_dict = {'gradebook': [
    {'student_id':1, 'name':'Red', 'grades':'A'},
    {'student_id':2, 'name':'Green', 'grades':'B'},
    {'student_id':3, 'name':'White', 'grades':'A'}
]}

import json
with open('grades.json','w') as grade:
    json.dump(grades_dict,grade)

with open('grades.json','r') as grade:
    print(json.dumps(json.load(grade),indent=4))

