class person:
    name = 'sakshi'
    occupation = 'software developer'

    def info(self):
        print(f"{self.name} has the occupation of {self.occupation}")
a=person()
a.info()

# better option
# use constructors

class person:
    def __init__(self):
        print("HI!! Sakshi here")

    def info(self):
        print(f"{self.name} has the occupation of {self.occupation}")
a=person() 
b=person()
# object create hote hi constructor call hogaya
# constructor with self parameter yahape usne sirf object ko parameter liya and fir 
# call hogaya

class person:
    def __init__(self,name,occ): #constructor with parameter
        self.name=name
        self.occupation=occ
    def info(self):
        print(f"{self.name} has the occupation of {self.occupation}")
a=person('sakshi','developer') 
a.info()
b=person('harry','accountant')
b.info()
