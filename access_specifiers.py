# public variable(default)
class employee:
    def __init__(self):
        self.name='Sakshi'

a=employee()
print(a.name)

# //private
class employee2:
    def __init__(self):
        self.__name='Sakshi'
        # private variables start with __

a1=employee2()
# print(a1.name)
# solution
print(a1._employee2__name) 
# method to access private variables

# protected
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())