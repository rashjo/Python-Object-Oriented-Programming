# parent class: Dog
class Dog:
    species = 'Canis familiaris' #Class Attributes
    
    def __init__(self, name, age): #Instance Attributes (Methods)
        self.name = name
        self.age = age
   
    def __str__(self):  # Instance Method
        return f'{self.name} is {self.age} years old'
    
    def speak(self, sound): # another instance method
        return f'{self.name} says {sound}'

# 3 CHILD class (JackRussellTerrier, Dachshund, Bulldog)
class JackRussellTerrier(Dog):
    pass  # do nothing (dont have attribute & method)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.age)
print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))
print(type(miles))
print(isinstance(miles,Dog))
print(isinstance(miles,JackRussellTerrier))

# isinstance(miles,Dog)  --function to check true/false
# isinstance(miles,JackRussellTerrier)
# miles.age
# miles.species
# buddy.name





