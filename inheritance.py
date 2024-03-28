class Car: # Creating the parent class.
    def __init__(self, name, color):
        """Used to initialize the attributes for new instances/objects of the class Car.

        Args:
            name (string): Takes a string as an argument which is then initialized as the 'name' attribute of the object.
            color (string): Takes a string as an argument which iss then initialized as the 'color' attribute of the object.
        """
        self.name = name
        self.color = color
    
    def carr(self):
        """Prints a formatted string that shows the name and the color of the current object.
        """
        print(f'{self.name} is a {self.color} supercar.')


class Lambo(Car): # Child class that inherits from the parent class 'Car'.
    def car_name(self):
        print(f"{self.name} is a Lamborghini")

car1 = Lambo('Huracan', 'Blue') # Creating an object 'car1' of the child class.
car1.carr() # Calling the method 'carr' of the parent class which prints the formatted string using the attributes of 'car1'.
car1.car_name() # Calling the additional method 'car_name' specific to the child class.
print(car1.name) # Accessing the attribute 'name' which was inherited from the parent class.
print(car1.color) # Accessing the attribute 'color' which was also inherited from the parent class.