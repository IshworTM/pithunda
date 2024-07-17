#class in python

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

person = Person("Dave", 35)
person2 = Person("hariramkrishnajaganathampremanandi", 49)
# hasattr example
setattr(person, "color", "blue")
setattr(person, "height", 180)  # setattr example
if hasattr(person, "name"):
    print(getattr(person, "name"))  # getattr example
print(person.name, person.age, person.height, person.color)
print(person2.name, person2.age)
if hasattr(person2, "color"):
    print("No")
else:
    print("Rip")


