# function  : block of code execute on calling


# def functionName(parameter):
#     execute
#     return

# functionName(argument)



# def display():
#     print("hello")

# display()
# display()
# display()
# display()
# display()
# display()
# display()


# no para no return 
def show():
    print("Good morning")

show()
# no para yes return 
def add():
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))
    return num1 + num2

# ans = add()
# print(ans)
print(add())

# yes para no return

def subtraction(num1, num2):
    print("Ans :",num1 - num2)

subtraction(12, 34)
subtraction(34, 34)
subtraction(340, 0)

# yes para yes return

def mul(num1 , num2):
    return num1 * num2

print(mul(12,0))
print(mul(12, 10))


# default , *argus , **kwargus



def add(num1 = 100 , num2 = 0):
   print("Add :",num1 + num2)


add(12, 1)
add(1)
add()



# *argus :


def show(*anything):
   print(anything)

show()
show(1)
show(1,2,3,4,5,6,7)


# **kwargus :
def info(**kwargus):
   print(kwargus)



info()
info(id = 1)
info(id = 1 , name = "user1", salary = 45000)





# recursion function :  function calling itself


def show(count):
   if(count == 0):    # base condition
      return
   print("Hello")
   show(count - 1)
show(10)


# print 1 to 10 , 10 to 1

def show_number(n):
   if n > 10:
      return
   print(n)
   show_number(n + 1)
show_number(1)

#print 10 to 1

def shownumber(n):
   if n < 1:
      return
   print(n)
   shownumber(n - 1)
shownumber(10)

# 1.Write a Python function to find the maximum between two numbers.


def add():
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))
    return num1 + num2

# ans = add()
# print(ans)
print(add())

#2. Write a Python function to find the maximum between three numbers.

def maxi_find():

 num1 = int(input("Enter the first number:"))
 num2 = int(input("Enter the second number: "))
 num3 = int(input("Enter the third number:"))

 if(num1 > num2 and num1 >= num3):
    print("max",num1)
 elif(num2 > num3  and  num2 >= num3):
    print("max",num2)
 else:
    print("max",num3)

maxi_find()

#3. Write a Python function to check whether a number is negative, positive,
#or zero.

def check_number(num):
   if num > 0:
      return "Positive"
   elif num < 0:
      return "Negative"
   else:
      return "Zero"
   
number =int(input("Enter a number:"))

print(check_number(number))

#4. Write a Python function to check whether a number is divisible by 5 and
#11 or not.

def divi_number(num):
   if num % 5 == 0 and num % 11 == 0:
      return " the values divisible by 5 and 11"
   else:
      return "the values not divisible bby 5 and 11"

number = int(input("Enter a number:"))
 
print(divi_number(number))

#5.Write a Python function to check whether a number is even or odd.

def even_odd_numbers(num):
   if num % 2 == 0:
      return "even"
   else:
      return "odd"
number = int(input("Enter a number:"))
print(even_odd_numbers(number))

#6.Write a Python function to check whether a character is an alphabet or
#not.

def alpha_bet(char):
   if(char >='a' or char <='z' and char >='A' or char <='Z'):
      return "character a alphabet... "
   else:
      return "character a not alphabet..."
   
character =input("Enter a charcter:")
print(alpha_bet(character))

#7.Write a Python function to input any alphabet and check whether it is a
#vowel or consonant.

def alpha_bet_vowel(char):
 if(character =="a" or character =="e" or character =="i" or character =="o" or character =="u"):
    return "vowel" 
 else:
    return "consonant"
 
character =input("Enter a character:")
print(alpha_bet_vowel(character))


#8.Write a Python function to input any character and check whether it is an
#alphabet, digit, or special character.

 
def check_character(chr):
    if len(chr) !=1:
       return "Enter a single character"
    if chr.isalphabet():
       return "Alphabe"
    elif chr.isdigit():
       return "Digit"
    else:
       return "Special character"
    
ch =input("Enter a character:")
print(check_character(chr))
       

#10.Write a Python function to check whether a character is uppercase or
#lowercase alphabet.

def check_char(char):
   
 if(char.isupper()):
    return "the character is uppercase"
 elif(char.islower()):
    return "the character is lowercase"
 else:
     return "it's not an alphabet character....."

ch =input("Enter a numner:")
print(check_char(ch))

#11.Write a Python function to input a week number and print the weekday.

def weekday(day):
   if day == 1:
      print("monday")
   elif day == 2:
      print("tuesday")
   elif day == 3:
      print("wednesday")
   elif day == 4:
      print("Thursday")
   elif day == 5:
      print("Friday")
   elif day == 6:
      print("Saturday")
   elif day == 7:
      print("sunday")
   else:
      print("Invalid week number! Please enter a number between 1 and 7.")

number =int(input("Enter weekday number (1 - 7):"))
weekday(number)

#12.Write a Python function to input a month number and print the number
#of days in that month.

def month_days():
    month = int(input("Enter month number (1-12): "))

    if month == 1:
        print("31 days")
    elif month == 2:
        print("28 or 29 days")
    elif month == 3:
        print("31 days")
    elif month == 4:
        print("30 days")
    elif month == 5:
        print("31 days")
    elif month == 6:
        print("30 days")
    elif month == 7:
        print("31 days")
    elif month == 8:
        print("31 days")
    elif month == 9:
        print("30 days")
    elif month == 10:
        print("31 days")
    elif month == 11:
        print("30 days")
    elif month == 12:
        print("31 days")
    else:
        print("Invalid month number")

month_days()


#14.Write a Python function to input marks of five subjects (Physics, Chemistry,
#Biology, Mathematics, and Computer), calculate percentage, and grade
#according to the following:
#15.Percentage >= 90% : Grade A
#16.Percentage >= 80% : Grade B
#17.Percentage >= 70% : Grade C
#18.Percentage >= 60% : Grade D
#19.Percentage >= 40% : Grade E
#20.Percentage < 40% : Grade F





