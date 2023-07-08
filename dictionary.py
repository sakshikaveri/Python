student={'name':'Sakshi', 'age':'21','gender':'female'}
# two methods to access single values of the dictionary
print(student['name'])
print(student.get('name'))
# methods to access all key values or all values only
print(student.keys())
print(student.values())

print(student.items())
for i,j in student.items():
    print(f"The value for key '{i}' is {j}")


