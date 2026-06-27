# Solution for Assignment-2 | Classes and Objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
        
    def setRadius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative!")
        self.radius = radius
    
    def getArea(self):
        return 3.14 * self.radius ** 2
    
    def getCircumference(self):
        return 2 * 3.14 * self.radius
    
class Rectangle:
    def __init__(self):
        pass

    def setDimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def showDimensions(self):
        print(f"Length: {self.length}, Breadth: {self.breadth}")

    def getArea(self):
        return self.length * self.breadth

class Book:
    def __init__(self, bookId, title, price):
        self.bookId = bookId
        self.title = title
        self.price = price

    def show_info(self):
        print(f"Id: {self.bookId}, Title: {self.title}, Price: {self.price}")

class Team:
    def __init__(self):
        self.member_names = []
    def input_members(self):
        while True:
            name = input("Enter name(enter 'done' to quit): ").strip()
            if name.lower() == 'done':
                break
            if name:  # Ensures empty strings are not added
                self.member_names.append(name)
    def display_member(self):
        if not self.member_names:
            print("The team currently has no members.")
        else:
            print("\n--- Team Members ---")
            for i in range(len(self.member_names)):
                print(f"{i+1}. {self.member_names[i]}")

# Test 
p = Person("Raju", 22)
p.show()

c = Circle(5)
print(f"Radius: {c.getRadius()}")
print(f"Area: {c.getArea():.2f}")
print(f"Circumference: {c.getCircumference():.2f}")

# c.setRadius(-5) 
# ValueError: "Radius cannot be negative!"

r = Rectangle()
r.setDimensions(5, 7)
r.showDimensions()
print(f"Area: {r.getArea()}")

b = Book(9301230, "Bernoulli\'s Equation", 530)
b.show_info()

t = Team()
t.input_members()
t.display_member()

