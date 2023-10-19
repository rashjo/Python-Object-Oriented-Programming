# Exercise 1a
# The parent 'Dog' class (given in exercise)
class Dog:
    species = "Canis familiaris"   # this is Class Attributes
    
    def __init__(self, name, age):  # Instance Attributes (Methods)
        self.name = name
        self.age = age
     
    def __str__(self):     #This is Instance Method
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):   #This is another instance method
        return f"{self.name} says {sound}"
    
# GoldenRetriever class
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

tramp = GoldenRetriever('Tramp', 6)

print(tramp.speak())
