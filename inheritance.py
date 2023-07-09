class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print(f"The name of the employee {self.id} is {self.name}")
class programmer(employee):
    def show(self):
        print("The default programming language is Python")

a=programmer('sakshi',56)
a.show()
a=employee('sakshi',56)
a.show() #error