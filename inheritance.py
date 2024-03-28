class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def carr(self):
        print(f'{self.name} is a {self.color} supercar.')


class Lambo(Car):
    def car_name(self):
        print(f"{self.name} is a Lamborghini")

car1 = Lambo('Huracan', 'Blue')
car1.carr()
car1.car_name()
print(car1.name)
print(car1.color)