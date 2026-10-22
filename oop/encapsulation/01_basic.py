# encapsulation  

# private(only can be used within the class) / public(can be use outside the class) / protected(can be use in drive class)


class Bank:
    def __init__(self, accountNumber,name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.__balance = balance  ## use double underscore to create private variable

    def display(self):
        print("Welcome : ",self.name)

    def balance(self):
        print("Your balance : ",self.__balance)

    def deposite(self,amount):
        self.__balance += amount
        print(amount,"deposite successfully")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient balance")


    
# withdrawl() , deposite

u1 = Bank(1,"user1", 5000)
u1.display()
print(u1.accountNumber)
print(u1.name)
# print(u1.__balance)
u1.balance()

print(u1.deposite(2000))
u1.balance()


print(u1.withdraw(3000))
u1.balance()

u1.withdraw(10000)



# encapsulation question
#  1.Create a class Student with attributes name, roll_no, and marks. Add a display() method to print
# student details.

class student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("name:",self.name)
        print("Roll_no:",self.roll_no)
        print("Marks:",self.marks)

s1= student("ishi",24,86)
s1.display()

#2 Create a Rectangle class with length and width. Add methods to calculate area and perimeter.

class rectangle:
    def __init__(self,length,width):
        self.length =length
        self.width =width

    def area(self):
        return(self.length * self.width)

    def perimeter(self):
        return 2*(self.length + self.width)        
r1 = rectangle(10,5)
print("Area",r1.area())
print("perimeter",r1.perimeter())


# 3 Create a BankAccount class with a public account_holder and private __balance. Add
# deposit(), withdraw(), and show_balance() methods.

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.__balance = balance
    
    def deposite(self,amount):
        self.__balance += amount
        print(amount,"deposite successfully")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance",self.__balance)

    
b1 = BankAccount("user1", 5000)

b1.show_balance()
b1.deposite(2000)
b1.withdraw(1000)
b1.show_balance()
    


#4 Create an Employee class with name and private __salary. Add set_salary() and get_salary()
#methods with salary validation.

class employee:
    def __init__(self,name):
        self.name = name
        self.__salary = 30000
    def set_salary(self,salary):
        if salary > 0:
            self.set_salary=salary
    def get_salary(self):
        return self.__salary
    

e1= employee("ishi")

e1.set_salary(30000)

print("Salary:",e1.get_salary())

# 5 Create a Book class with title, author, and private __stock. Add add_stock(), sell_book(), and
# display_details() methods.

class Book:
    def __init__(self, title, author, stock):
        self.title = title
        self.author = author
        self.__stock = stock

    def add_stock(self, quantity):
        self.__stock += quantity

    def sell_book(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            print(quantity, "book(s) sold")
        else:
            print("Not enough stock")

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Stock:", self.__stock)


b1 = Book("Python Programming", "John", 20)

b1.display_details()
b1.add_stock(10)
b1.sell_book(5)
b1.display_details()