#actual thing shwing outside but it defined by class how it's gonna look
#oops started 
#class is the blue print specify variable and function
class car:
    #The __init__method set up attributes for every new car
    def __init__(self, brand, color, max_speed):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed#these are attributes
    #mow definig the function of the car
    def drive(self):
        print(f"The {self.color} {self.brand} goes vroom!")
#The objects
car1 = car("Tesla", "Red", 270)
car2 = car("mercedes", "Black", 320)
#accessing the object
print(car1.color)
print(car2.brand)

car1.drive()
car2.drive()