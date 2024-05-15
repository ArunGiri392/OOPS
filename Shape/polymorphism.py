class Shape:
    pie = 3.14
    def __init__(self):
        pass

    def area(self):
        pass

class Circle(Shape):
     def __init__(self, radius):
        self.radius = radius

     def area(self):
        print("i am from circle")
        return Shape.pie * self.radius * self.radius

class Rectangle(Shape):
     def __init__(self, length, breadth):
        
        self.__length = length
        self.__breadth = breadth
    
     def area(self):
        print("i am from rectangle")
        return self.__length * self.__breadth

def printarea(Shape):
    print(Shape.area())

circle = Circle(2)
rectangle = Rectangle(3,4)

printarea(circle)
printarea(rectangle)
# This demonstrates polymorphism because the print_area function works with objects of different types (both Circle and Rectangle) through a common interface (Shape). 
# The actual method called idetermined at runtime baseds  on the type of the object, showcasing the flexibility and adaptability of polymorphism.