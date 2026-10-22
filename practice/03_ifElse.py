#if Else stetement
age = 45

if(age < 50):
    print("Adult",age)
else:
    print("Child", age)

#user input 

age = int(input("Enter your age :")) # type casting

if(age > 18):
    print("Adult",age)
else:
    print("child",age)

# 1. Write A python Program To Find Maximum Between Two Numbers.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if(num1 > num2):
    print("Max",num1)
else:
    print("Max",num2)


#2. Write A python Program To Find Maximum Between Three Numbers.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the secode number:"))
num3 = int(input("Enter the third number:"))

if(num1 > num2  and num1 >= num3):
    print("Max ",num1)
elif(num2 > num1  and num2 >= num3):
    print("Max",num2)
else:
    print("Max",num3)


#3. Write A python Program To Check Whether A Number Is Negative, Positive Or Zero.

num = float(input("Enter a Number:"))


if(num > 0):
    print("The Number is a Positive", num)
elif(num < 0):
    print("The Number is a Negative", num)
else:
    print("the number is a Zero", num)


#4. Write A python Program To Check Whether A Number Is Divisible By 5 And 11 Or Not.

num = int(input("Enter a number is Divisible : "))

if(num % 5 == 0 and num % 11 == 0):
    print("the number is divisible by 5 and 11 ", num)
else:
    print("the number is not divisible by 5 and 11 ",num)




# 5. Write A C Program To Check Whether A Number Is Even Or Odd.
# even  : 2, 4 , 6, 8, 10 ,12....
# odd  : 1 , 3, 5, 7 , 9, 11 ......

num = int(input("Enter a number : "))

if(num % 2 == 0):
    print("Even : ", num)
else:
    print("Odd : ",num)




# 6. Temperature Check: Write a Python program that takes the temperature
# as input. If the temperature is above 30 degrees Celsius, print "It's a hot
# day!" Otherwise, print "It's a cool day."

temperture = float(input("the temperature is above 30 degrees celsius : "))

if (temperture > 30):
    print("it's a hot day!")
else:
    print("it's a cool day")

# 7. User Authentication: Create a program that asks the user to enter a
# username and password. If the username is "admin" and the password is
# "password123," print "Login successful." Otherwise, print "Invalid
# credentials."

username =input("Enter Username:")
password = input("Enter Password:")

if(username == "Admin" and password == "password123") :
    print("Login Successfull...")
else:
    print("Invalid credentials...!")

# 8. Write a Python program to check if a given year is a leap year or not.

year = int(input("Entercheck to year: "))

if(year % 4 == 0) :
    print("leap year ", year)
else:
    print("not leao year ", year)
# 9. Write a Python program to check if a given character is a vowel or a
# consonant

charactor = input("Enter a charactor : ")
if(charactor == "a" or charactor == "e"  or charactor == "i" or charactor == "o" or charactor == "u"):
    print("Vowel :", charactor)
else:
    print("Consonant : ",charactor)





# print(4 > 5 and 3 < 0 or 3 != 5 and 7 == 0 or 5 %3 == 0)



# 10. Write a Python program to input the age of a person and determine if
# they are eligible to vote (18 or older)


age = int(input("Enter the age: "))

if( age >= 18):
    print("Eligilble to vote...")
else:
    print("Eligilble to not vote...! ")

# 11. Write a Python program to check if a given character is uppercase or
# lowercase.

char = input("Enter a character:")

if(char.isupper()):
    print("The character a uppercase...")
elif(char.islower()):
    print("The character a lowercase...")
else:
    print("it's not an alphabet character.....")


#12. Write a Python program to input a number representing a day of the
#week (1 for Monday, 2 for Tuesday, etc.) and print the corresponding day.


day = int(input("Enter a Number (1-7) :"))

if day == 1:
    print("monday",day)
elif day == 2:
    print("Tuesday",day)
elif day == 3:
    print("Wednesday",day)
elif day == 4:
    print("thrursday",day)
elif day == 5:
    print("friday",day)
elif day == 6:
    print("saturday",day)
elif day == 7:
    print("sunday",day)
else:
    print("invaild input!,pelase enter a number between 1 and 7 ....")

 
#13. Write a Python program to input the month number (1 for January, 2 for
#February, etc.) and print the number of days in that month (considering
#leap years)

month = int(input("Enter a month (1-12) :"))

if month == 1:
    print("January",month)
elif month == 2:
    print("February",month)
elif month == 3:
    print("March",month)
elif month == 4:
    print("April",month)
elif month == 5:
    print("May",month)
elif month == 6:
    print("June",month)
elif month == 7:
    print("july",month)
elif month == 8 :
    print("August",month)
elif month == 9 :
    print("September",month)
elif month == 10 :
    print("October",month)
elif month == 11:
    print("Noverber",month)
elif month == 12 :
    print("December",month)
else:
     print("invaild input!,pelase enter a month between 1 and 12 ....")




# 14. Write a Python program to input the marks of four subjects (out of 100)
# and calculate the average and determine the grade as follows:
# Average >= 90: Grade A
# Average >= 80: Grade B
# Average >= 70: Grade C
# Average >= 60: Grade D
# Average >= 50: Grade E
# Average < 50: Grade F





# subj1=input("Enter name of subject1:")
subj1 =float(input("Enter marks of subject1:"))

# subj2=input("Enter name of subject2:")
subj2 =float(input("Enter marks of subject2:"))

# subj3=input("Enter name of subject3:")
subj3 =float(input("Enter marks of subject3:"))

# subj4=input("Enter name of subject4:")
subj4 =float(input("Enter marks of subject4:"))

average =( subj1 + subj2 + subj3 + subj4) / 4

if average >= 90:
    print("Grade A", average)
elif average >= 80 :
    print("Grade B", average)
elif average >= 70 :
    print("Grade C", average)
elif average >= 60 :
    print("Grade D", average)
elif average >= 50 :
    print("Grade E", average)
else :
    
    print("Grade F", average)

# 15. Write a Python program to input the price of an item and the money
# given by the customer, then calculate and print the change to be returned.

productPrice = float(input("Enter product price :"))
money = float(input("Enter amount paid : "))

if(productPrice > money):
    print("Give ", productPrice - money)
elif(money > productPrice):
    print("Change ", money - productPrice)
else:
    print("Thank You")



