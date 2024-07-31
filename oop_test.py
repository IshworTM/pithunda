class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance and accessing special attributes:
person_instance = Person("John", 30)
print(person_instance.__class__.__name__)  # Output: Person
print(person_instance.__module__)          # Output: __main__

# Using getattr to retrieve attribute value:
attribute_name = 'age'
print(getattr(person_instance, attribute_name))  # Output: 30