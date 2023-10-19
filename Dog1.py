class Dog:
    # Class Attributes
    species = 'Canis familiaris'
    
    # Instance Attributes (Methods)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def description(self):
        return f'{self.name} is {self.age} years old'
    
    # Another instance method
    def speak(self, sound):
        return f'{self.name} says {sound}'

# create object
buddy = Dog ("Buddy", 9)
miles = Dog ("Miles", 4)

#print
print(buddy.name)
print(miles.age)
print(miles.description())
print(buddy.description())
print(miles.speak("woof woof"))
print(miles.speak("bow bow"))
print(miles)
print(buddy.speak("bow bow"))
