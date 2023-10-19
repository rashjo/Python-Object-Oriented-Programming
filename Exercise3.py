# Exercise 3
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        
    def drive(self, miles):
        self.mileage = self.mileage + miles
        
blue_car = Car("blue", 0)
blue_car.drive(100)

print(blue_car.mileage)
print(blue_car.drive(150))
print(blue_car.mileage)