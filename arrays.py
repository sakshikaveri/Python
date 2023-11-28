from array import *

values=array('i',[1,2,3,4,5])
print(values)
values=array('i',[1,2,-3,4,5])
print(values)
# values=array('I',[1,2,-3,4,5])  #error
# print(values)

print(values.buffer_info())  #address and length

