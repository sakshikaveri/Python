class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def makesound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self,name,breed):
        self.breed=breed
        Animal.__init__(self,name,species='Dog')

    def makesound(self):
        print('Bark!')


d=Dog('Dog','Dog')
d.makesound()

a=Animal('Dog','Doggerman')
a.makesound()