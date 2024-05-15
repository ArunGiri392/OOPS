class Shape:
    pie = 3.14
    def __init__(self, name):
        self.name = name

    # abstract method
    def area():
        pass

    # abstract method
    def perimeter():
        pass


class Rectangle(Shape):

    def __init__(self, length, breadth,name):
        super().__init__(
            name
        )
        self.__length = length
        self.__breadth = breadth
    
    def area(self):
        return self.__length * self.__breadth

    def perimeter(self):
        return 2*(self.__length + self.__breadth)


class Circle(Shape):
    
    def __init__(self,radius,name):
         super().__init__(
            name
        )
         self.__radius = radius
        

    def area(self):
        return Shape.pie * self.__radius * self.__radius

    def perimeter(self):
        return 2* Shape.pie * self.__radius

rectangle = Rectangle(4,5,"rectangle")
print("The area of " + rectangle.name + "is" + str(rectangle.area()))
print(rectangle.perimeter())


circle = Circle(4, "circle")
print(circle.area())
print(circle.perimeter())