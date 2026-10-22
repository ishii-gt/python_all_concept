# inheritance : accessing the parent class property 



class Parent:
    def car(self):
        print("Parent drive car!!!")



class Child(Parent):
    def bike(self):
        print("Child drive bike")


p = Parent()
p.car()

c = Child()
c.bike()
c.car()




# types of inheritance : simple inheritance , multiple inheritance , multi-level inheritance , hirarchical inheritance , hybrid inheritance


# multi-level
class GrandFather:
    def grandFather(self):
        print("grand father")

class Father(GrandFather):
    def father(self):
        print("father")

class Son(Father):
    def son(self):
        print("son")

g = GrandFather()
g.grandFather()

f = Father()
f.grandFather()
f.father()

s = Son()
s.father()
s.grandFather()
s.son()



# mulitple inheritance

class Father:
    def father(self):
        print("father")

class Mother :
    def mother(self):
        print("mother")

# ambiguity 

class Son(Father, Mother):
    def son(self):
        print("son")

s = Son()
s.father()
s.mother()
s.son()


# hierarchial inheritance:

class Father:
    def father(self):
        print("father")
    # pass

class Son1(Father):
    def son1(self):
        pass

class Son2(Father):
    # pass
    def son2(self):
        print("son2")


s1 = Son1()
s1.son1()
s1.father()

# s2 = Son2()
# print(type(s2))




# hybrid  inheritance


#    A
#   / \
#  B   C
#   \ /
#    D


class A:
    pass

class B(A):
    pass
class C(A):
    pass
class D(C,B):
    pass


# mro  :method resolution order

print(D.mro())

# (BASIC INHERITANCE)
# 1. Define a class Animal with attributes name and sound. Derive a class 
# Dog from Animal with an additional attribute breed. Create instances 
# of Dog and demonstrate inheritance.

class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    
    def display(self):
        print("name",self.name)
        print("sound",self.sound)

class Dog(Animal):
    def __init__(self, name, sound,breed):
        self.name = name
        self.sound = sound
        self.breed = breed

    def __init_subclass__(self,name,sound,breed):
        super().__init_subclass__(name,sound)
        self.breed = breed

    def display_dog(self):
        self.display()
        print("breed",self.breed)

d1 = Dog("Jack","Bark","German Shepherd")
d1.display_dog()


# Multilevel Inheritance:

# Define a class Vehicle with attributes brand and year. Derive classes Car 
# and Bike from Vehicle. Further derive classes SportsCar from Car and 
# MountainBike from Bike. Show how attributes propagate through the 
# inheritance chain

class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year,fuel_type):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

class Bike(Vehicle):
    def __init__(self, brand, year,bike_type):
        super().__init__(brand, year)
        self.bike_type = bike_type


class SportsCar(Car):
    def __init__(self, brand, year, fuel_type,speed):
        super().__init__(brand, year, fuel_type)
        self.speed = speed

    def display(self):
        print("Brand : ",self.brand)
        print("Year : ",self.year)
        print("Fuel : ",self.fuel_type)
        print("Speed : ",self.speed )

class MountainBike(Bike):
    def __init__(self, brand, year, bike_type,colour):
        super().__init__(brand, year, bike_type)
        self.colour = colour

    def display(self):
        print("Brand :",self.brand)
        print("Year : ",self.year)
        print("Bike Type : ",self.bike_type)
        print("Colour : ",self.colour)


car1 = SportsCar("Benz",2025,"Petrol",250)
bike1 = MountainBike("Royal Enfield",2025,"Mountain Bike","Matt Brown")

car1.display()
print("Car Details Displayed")
bike1.display()
print("Bike Detail Displayed")


# Hierarchical Inheritance


# Define a class Person with attributes name and age. Derive classes 
# Student and Teacher from Person. Implement methods study() in 
# Student and teach() in Teacher. 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def study(self):
        print(self.name,"is doing Study")
        print("My age is",self.age)
    

class Teacher(Person):
    def teach(self):
        print(self.name,"is teaching")
        print("My age is ",self.age)

Student1 = Student("Krish",22)
Teacher1 = Teacher("Hemang Sir",30)

print(Student1.name)
print(Student1.age)
Student1.study


print(Teacher1.name)
print(Teacher1.age)
Teacher1.teach






# Multiple Inheritance: 
# 6. Create classes A, B, and C. Class A has method display_A(), class B has 
# method display_B(), and class C inherits from both A and B, 
# implementing display_C() that calls both parent methods.

class A:
    def A(self):
        print("Hi I am class A")

class B:
    def B(self):
        print("Hi I am class B")

class C(A,B):
    def C(self):
        print("I can Access Both A and B")
        

C = C()
C.B()
C.A()
C.C()

    
# 1. Employee Management System (Single Inheritance)
# Create a base class Employee with employee_id, name, salary and display_details(). Create
# Developer inheriting Employee with programming_language and write_code(). Task: Create 3
# developers, display details, calculate annual salary.


class Employee:
    def __init__(self,employee_id,name,salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
    
    def display_details(self):
        print("Employee_id : ",self.employee_id )
        print("My Name is : ",self.name)
        print("My Salary is : ",self.salary)


class Developer(Employee):
    def __init__(self,employee_id,name,salary,programming_language):
        super().__init__(employee_id,name,salary)
        self.programming_language = programming_language

    def write_code(self):
        print("Programming Language is : ",self.programming_language)

    def annuayl_salary(self):
        return self.salary * 12
    
d1 = Developer(1,"Krish",20000,"Python")
d2 = Developer(2,"User2",21000,"Java")
d3 = Developer(3,"User3",22000,"C++")

d1.display_details()
print("Programming Language : ",d1.programming_language)
print("Annual Salart is : ",d1.annuayl_salary())

print("+++++++++++++++++++++++++++++++++++++++++++++")


d2.display_details()
print("Programming Language : ",d2.programming_language)
print("Annual Salart is : ",d2.annuayl_salary())


print("+++++++++++++++++++++++++++++++++++++++++++++")

d3.display_details()
print("Programming Language : ",d3.programming_language)
print("Annual Salart is : ",d3.annuayl_salary())


print("+++++++++++++++++++++++++++++++++++++++++++++")

# 2. E-Commerce Platform (Multilevel Inheritance)
# User -> Customer -> PremiumCustomer hierarchy. Implement login(), add_to_cart(),
# apply_discount(). Task: Add products and calculate final discounted bill.

class User:
    def __init__(self,username):
        self.username = username
    
    def login(self):
        pass

    def add_to_cart(self,product,price):
        # self.product = product
        # self.price = price
        print("Product aded")
    # def 
    def dicount(self):
        pass

    def display(self):
        print("Username : ",self.username)

class Customer(User):
    def __init__(self,username):
        super().__init__(username)

    def login(self):
        print("Welcome normal user")

    def dicount(self):
        print("5%")



class PremiumCustomer(Customer):
    def __init__(self,username):
        super().__init__(username)
    def login(self):
        print("Welcome premium user")
    def dicount(self):
        print("15%")




c = Customer("user1")
pc = PremiumCustomer("user2")

    
pc.dicount()
    








# 3. Payment Gateway System (Multiple Inheritance)
# CreditCardPayment and UPIPayment classes. HybridPayment inherits both. Task: Validate
# payment method and implement make_payment(amount).


class CreditCardPayment:
    def creaditCard(self,amount):
        print(f"Payment Done through Credit Card : ${amount}")    

class UPIPayment:
    def upi(self, amount):
        print(f"Payment Done through UPI : ${amount}")    
    


class HybridPayment(CreditCardPayment,UPIPayment):
    def payment_validate(self,paymentMethod, amount):
        if(paymentMethod.lower() == "creditcard"):
            self.creaditCard(amount)
        elif(paymentMethod.lower() == "upi"):
            self.upi(amount)
        else:
            print("Invalid payment gateway")

upi1 = HybridPayment()
upi1.payment_validate("upi", 450)
cc1 = HybridPayment()
cc1.payment_validate("creditcard", 34)





            