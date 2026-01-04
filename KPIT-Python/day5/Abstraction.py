from abc import ABC, abstractmethod

#import abc as a

# abc- module name
# ABC- class name , to mark our class as abstract
# abstarctmethod - a decorator which is used to mark method as abstract method

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
    
class Myclass(ABC):    
    @abstractmethod
    def hello(self):
        pass
    
    def hello2(self):
         print('In Myclass')
         
class Child(Myclass):
    def hello(self):
        print('hello from child class')
        
m1=Child()
m1.hello()
m1.hello2()

# Attempting to instantiate the abstract class will raise an error
try:
    shape = Shape()
except TypeError as e:
   print(e)

# Instantiating the concrete classes works fine
circle = Circle(5)
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")

'''
class Shape:
   void draw(self): .....


class Circle(Shape)
    

class BigCircle(Circle)
     

c1=Circle()
c1.draw()



def add(a,b):
   -----

def add(a,b,c,d):
   ----

add(10,20)

add(1,2,3,4)
'''