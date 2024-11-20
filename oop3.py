class Ember:
    def __init__(self, name, age, height, weight,):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def getStuff(self):
            print(self.name)
            print(self.age)
            print(self.height)
            print(self.weight)
        

ember = Ember('Jabud', 17, 180, 200)
print(ember.getStuff())