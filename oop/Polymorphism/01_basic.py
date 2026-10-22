# method over riding , method overloading



# method over loading : same method name within same class but different parameter 


# class Shape:

#     def area(self, height, width):
#         print(height * width)
#     def area(self,height , width , length = 1):
#         print(height * width * length)


# s = Shape()
# s.area(23 , 34)
# s.area(23 , 34, 10)



# method over riding : same method name but in different class



# super()

class GrandFather:
    def vehicle(self):
        print("Train")
class Parent(GrandFather):
    def vehicle(self):
        super().vehicle()
        print("Car")
    def display(self):
        print("hello parent")
class Son(Parent):
    def vehicle(self):
        super().vehicle()
        super().display()
        print("cycle")


s = Son()
s.vehicle()




# dunder  

class Special:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
    



s1 = Special("User1")
# print(s.name)
s2 = Special("user2")

print(s1)
print(s2)

print(12 +13)

class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return self.num + other.num

n1 = Number(12)
n2 = Number(13)
print(n1 + n2)   # n1.__add__(n2)

class Coordinates:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return [self.x + other.x, self.y + other.y , self.z + self.z]
        # return "Addition called"
    

p1 = Coordinates(1,2,3)
p2 = Coordinates(2,3,4)
print(p1 + p2)

# - -> __sub__()
# len() -> __len__()
# > -> __gt__()
