# from model import AnotherShape
# obj2 = AnotherShape()g
# print(type(obj2))

# oop  : object oreinted programming



# class : blueprint
# obj : real entity
# constructor : special method that execute on without calling (when you make a obj)

# dunder method 
class Shape:
    def __init__(self):
        print("Constructor called")

    def display(self):
        print("I am shape")
    


obj = Shape()
obj.display()




class Rectangle:
    def __init__(self, length , breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area : ", self.length * self.breadth)

r1 = Rectangle(10,10)
r1.area()



r2 = Rectangle(20, 10)
r2.area()
        


