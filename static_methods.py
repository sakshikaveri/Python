# public variable(default)
class employee:
    def __init__(self):
        self.name='Sakshi'
    @staticmethod
    def add(a,b):
        return a+b

        

a=employee()
print(a.name)
print(a.add(4,5))
print(employee.add(4,5))
# add(4,5) error