

def cube(x):
    return x*x*x
print(cube(2))

l=[1,2,3,4,5]
newl=[]
for i in l:
    newl.append(cube(i))
print(newl)

# MAP
newnewl=list(map(cube,l))  
# map ko function and jispe iterate hona chhaiye vo parameter(yahape list)
print(newnewl)
print(type(newnewl))

# filter
def filter_function(item):
    return item>1
new_list=list(filter(filter_function,l)) 
# yahape filter function value dega either true/false, agar true hua tho baju ka parameter ka value ajayga variable me
print(new_list)

# reduce
from functools import reduce
numbers=[1,2,3,4,5,6]
last=reduce(lambda x,y:x+y, numbers)
print(last)

