
# Python Function practice

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








# Python Recursion practice

# 1. Write a Python function to calculate the factorial of a number using recursion.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter factorial number:"))
print("Factorial:", factorial(num))

# 2. Write a Python function to compute the nth Fibonacci number using recursion.


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter factorial number:"))
print("Fibonacci number:", fibonacci(num))


# 3. Implement a recursive function to calculate the sum of digits of a number.


def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

num = int(input("Enter sum of digits:"))
print("Sum of digits:", sum_digits(num))


# 4. Write a recursive Python function to check if a given string is a palindrome.


def palindrome(s):
    if len(s) <= 1:         #base case 
        return 
    if s[0] != s[-1]:
        return 
    return palindrome(s[1:-1])

s = input("Enter a string:")

if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")

# 5. Create a recursive Python function to find the GCD (Greatest CommonDivisor) of two numbers.



def gcd(a, b):
    if a == b:
        return a
    if a > b:
       return gcd(a - b ,b)
    else:
        return gcd(a , b = b)

num1 =int  (input("Enter number1:"))
num2 =int  (input("Enter number2:"))

print("GCD:", gcd(num1, num2))

# 6. Write a recursive function to compute the power of a number.

def power(a , b):
    if b== 0:
        return 1
    else:
        return a * power(a ,b - 1)
a = int(input("Enter a number:"))
b = int(input("Enter b number:"))
power = int (input("Enter the power function :"))
print(power(a,b))


# 7. Develop a recursive function to reverse a string.

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

text = "hello ishii"
print(reverse(text))


# 8. Write a recursive function to generate all subsets of a set.

# 9. Create a recursive function to solve the combination sum problem, where
# given a set of candidate numbers and a target number, find all unique
# combinations that sum up to the target.



# 10.Write a recursive function to solve the subset sum problem, where given a
# set of non-negative integers and a target sum, determine if there is a
# subset that sums up to the target.