# Dunder (Magic) Methods

Dunders (double underscores) are some special methods in Python. They are also called magic methods. These methods are used to implement the behavior of operators in Python.

One of the most common dunder methods is the constructor `__init__` method. This method is used to initialize the object.

There is also a destructor `__del__` method. This method is used to delete the object.

Example 1:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} is being created")

    def __del__(self):
        print(f"{self.name} is being deleted")

person = Person("John", 25)
```

Output:
```
John is being created
John is being deleted
```

Note that the destructor is not called when the program ends, but only when the object is deleted. This is because the `__del__` method is called by the garbage collector when the object is deleted after the program ends. 

This also works with the `del` keyword.

```python
del person
```

In this case, the destructor is called when the object is deleted using the `del` keyword.

Let's see another example. Let's create a Vector class and add two vectors together. 

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)
```

Output:
```
TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
```

This is because, Python does not know how to add two objects with `+` operator. The `+` operator works with built-in types like int, float, etc.

To define how two `Vector` objects should be added, we need to implement the __add__ method in our Vector class. This method tells Python what to do when the `+` operator is used with Vector objects.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)
```

Output:
```
<__main__.Vector object at 0x0000022B23454E50>
```
The `__add__` method takes two arguments: `self` and `other`. 
`self` refers to the current instance of the class, which is `v1` in this case.
`other` refers to the second operand, which is `v2` in this case.

Note that the output is an object of the Vector class. This is because the `__add__` method returns a new Vector object.

To clearly view the output, we can modify the `__str__` or `__repr__` method in our Vector class.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3)
```

Output:
```
Vector(4, 6)
```

If we call `print(repr(v3))`, we will get the same output as:
```
Vector(x=4, y=6)
```

But what is the difference between `__str__` and `__repr__`?

The `__str__` method is used to return a string representation of the object. This is the string that you see when you print the object.

The `__repr__` method is used to return a string representation of the object. This is the string that you see when you use the `repr()` function. The sole purpose of `__repr__` is to be unambiguous representation of the object, where developer can understand the object.

Here are some more examples of dunder methods:

1. Comparison Operations:
   - `__eq__(self, other)`: Defines behavior for the `==` operator.
   - `__lt__(self, other)`: Defines behavior for the `<` operator.
   - `__le__(self, other)`: Defines behavior for the `<=` operator.

   ```python
   class Box:
       def __init__(self, volume):
           self.volume = volume

       def __eq__(self, other):
           return self.volume == other.volume

       def __lt__(self, other):
           return self.volume < other.volume
   
   b1 = Box(10)
   b2 = Box(15)
   print(b1 == b2)  # False
   print(b1 < b2)   # True
   ```

2. Length and Indexing:
   - `__len__(self)`: Defines behavior for the `len()` function.
   - `__getitem__(self, key)`: Defines behavior for indexing operations.

   ```python
   class CustomList:
       def __init__(self, items):
           self.items = items

       def __len__(self):
           return len(self.items)

       def __getitem__(self, index):
           return self.items[index]

   my_list = CustomList([1, 2, 3, 4])
   print(len(my_list))      # Returns 4
   print(my_list[2])        # Returns value at index 2, which is 3
   ```

3. Attribute Access:
   - `__getattr__(self, name)`: Defines behavior for attribute access.
   - `__setattr__(self, name, value)`: Defines behavior for attribute assignment.
   - `__delattr__(self, name)`: Defines behavior for attribute deletion.

   ```python
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
   ```

These are some of the most commonly used dunder methods, but there are many more you can explore, such as `__call__`, `__contains__`, `__iter__`, `__next__`, and `__hash__`, which provide even more customization to your classes.
