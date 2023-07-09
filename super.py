# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")
# class Parentclass2:
#     def parent_method2(self):
#         print("This is the parent method 2.")

# class ChildClass(ParentClass, Parentclass2):
#     def child_method(self):
#         print("This is the child method.")
# a=ParentClass()
# b=ChildClass()
# b.child_method()
# b.parent_method()
# b.parent_method2()

class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass2, ParentClass1):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
# yahape parent method of the parentclass2 print hoga kyuki bracket me voh pehle likha h