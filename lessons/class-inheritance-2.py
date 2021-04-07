# Class inheritance
# Code from pirple.com lesson in "Python is Easy"
# Typed up by Franz A. Tapia Chaca
# 07 April 2021

class Pet:
    def __init__(self, name_set, age_set, hunger_set, playful_set):
        self.name = name_set
        self.age = age_set
        self.hunger = hunger_set
        self.playful = playful_set

    # Setters
    def setName(self, name_set):
        self.name = name_set

    def setAge(self, age_set):
        self.age = age_set

    def setHunger(self, hunger_set):
        self.hunger = hunger_set

    def setPlayful(self, playful_set):
        self.playful = playful_set

    # Getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful


class Dog(Pet):
    def __init__(self, name_set, age_set, hunger_set, playful_set, breed_set, favouriteToy_set):
        Pet.__init__(self, name_set, age_set, hunger_set, playful_set)
        self.breed = breed_set
        self.favouriteToy = favouriteToy_set

    def wantsToPlay(self):
        if self.playful:
            return "Dog wants to play with " + self.favouriteToy + "."
        else:
            return "Dog doesn't want to play."


Pet1 = Pet("Peter", 3, False, True)

# Accessing and changing the name of object in the parent class Pet
print(Pet1.getName())
Pet1.setName("Snowball")
print(Pet1.getName())
print(Pet1.name)
Pet1.name = "Jim"
print(Pet1.name)

# Manipulating object in the inherited class Dog
huskyDog = Dog("Snowball", 5, False, True, "Husky", "stick")
Play = huskyDog.wantsToPlay()
print(Play)
huskyDog.playful = False
print(huskyDog.wantsToPlay())
