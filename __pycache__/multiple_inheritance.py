class Family:
	def show(self):
		print("My Family....") 
 
class Father(Family):
	name_father = ""

	def show1(self):
	    print(self.name_father) 
 
class Child(Father):
	name_child = ""

	def show2(self):
		print("Father Name :",self.name_father)
		print("Child Name : ",self.name_child)
 
o = Child()
o.name_father = "Sumit"
o.name_child = "Rajat"
o.show()
o.show2()
