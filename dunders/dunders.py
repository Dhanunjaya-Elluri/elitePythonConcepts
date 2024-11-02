# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"{self.name} is being created")

#     def __del__(self):
#         print(f"{self.name} is being deleted")

# p = Person("John", 30)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __str__(self):
#         return f"Vector({self.x}, {self.y})"
    
#     def __repr__(self):
#         return f"Vector(x={self.x}, y={self.y})"

# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)

# print(repr(v3))

class Animal:
    def __init__(self, species):
        self.species = species

    def __getattr__(self, name):
        return f"No attribute named '{name}' found"

    def __setattr__(self, name, value):
        if name == "species" and not isinstance(value, str):
            raise ValueError("Species must be a string")
        super().__setattr__(name, value)

animal = Animal("Dog")
print(animal.species)  # Dog
print(animal.color)    # No attribute named 'color' found
