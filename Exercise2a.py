# Exercise 2a
# Rectangle and Square classes

class Rectangle: #parent class
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

class Square(Rectangle):  #child class
    def __init__(self, side_length):
        super(). __init__(side_length, side_length)

#create object of rectangle
#Area of rectangle with length=3, width=5
rectangle = Rectangle(3,5)
print(rectangle.area())

square = Square(4)
print(square.area())



