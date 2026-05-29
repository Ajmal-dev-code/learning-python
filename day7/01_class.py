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
