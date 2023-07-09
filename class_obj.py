
class person:
    name = 'sakshi'
    occupation = 'software developer'

    def info(self):
        print(f"{self.name} has the occupation of {self.occupation}")


a = person()
# print(a.name)
# print(a.occupation)
print(f"{a.name} is a {a.occupation}")
a.info()


b = person()
b.name = 'pooja'
b.occupation = 'analyst'
print(f"{b.name} is a {b.occupation}")
b.info()

c = person()
c.name = 'nikita'
c.info()
