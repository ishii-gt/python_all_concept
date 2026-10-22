# if Else: statement control
age = 55

if(age > 18):
    print("Adult",age)
else:
    print("Child", age)
    

# user input 

age = int(input("Enter your age :"))  # type casting

# print(age)
# print(type(age))

if(age > 18):
    print("Adult :", age)
else:
    print("Child :", age)



# 1. Write A python Program To Find Maximum Between Two Numbers.

num1 = int(input("Enter first number : ")) # 12
num2 = int(input("Enter second number :")) # 33

if(num1 > num2):
    print("Max :",num1)
else:
    print("Max :",num2)

#2. Write A python Program To Find Maximum Between Three Numbers.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number: ")) 
num3 = int(input("Enter the third number:"))

if(num1 > num2 and num1 >= num3):
    print("max",num1)
elif(num2 > num3  and  num2 >= num3):
    print("max",num2)
else:
    print("max",num3)

#3. Write A python Program To Check Whether A Number Is Negative, Positive Or Zero.

num = float(input("Entet Number: "))

if(num > 0):
    print("The number is a positive",num)
elif(num < 0):
    print("The number is a negative ",num)
else:
    print("The zero number :",num)


#4. Write A python Program To Check Whether A Number Is Divisible By 5 And 11
#Or Not.

num = int(input("Enter Number is Dicisible :"))

if(num % 5 == 0 and num % 11 == 0):
    print("Enter A number is divisible by 5 and 11..")
else:
    print("Enter A number is not divisible by 5 and 11..")


#5. Write A python Program To Check Whether A Number Is Even Or Odd.
# even = 2 ,4 ,6 ,8 , 10...
# odd = 1 ,3 ,5 ,7 ,9 , 11..

num = int(input("Enter number:"))
if(num % 2 == 0):
    print("even")
else:
    print("odd")

#6. Temperature Check: Write a Python program that takes the temperature
#as input. If the temperature is above 30 degrees Celsius, print "It's a hot
#day!" Otherwise, print "It's a cool day."

temperature = float(input("Enter the temperature is above 30 degrees celsius: "))

if(temperature > 30):
    print("It's a hot day")
else:
    print("It's a cool day")

#7. User Authentication: Create a program that asks the user to enter a
#username and password. If the username is "admin" and the password is
#"password123," print "Login successful." Otherwise, print "Invalid
#credentials."

username =input("Enter username:")
password = input("Enter password:")

if(username == "Admin" and password == "password123"):
    print("Login succesfully...")
else:
    print("Invalid credentials...!")

#8. Write a Python program to check if a given year is a leap year or not.

year =int(input("Entercheck year:"))

if(year % 4 == 0):
    print("leap year")
else:
    print("not leap year..!")

#9. Write a Python program to check if a given character is a vowel or a
#consonant

character = input("Enter a character :")
if(character == "a"or character == "e" or character == "i" or character == "o" or character == "u"):
    print("vowel",character)
else:
    print("consonant",character)

#10. Write a Python program to input the age of a person and determine if
# they are eligible to vote (18 or older)

age = int(input("Enter age:"))

if(age >= 18):
    print("Eligible to vote..")
else:
    print("Eligible to not vote..")


# 11. Write a Python program to check if a given character is uppercase or
# lowercase.

char = input("Enter the character:")

if(char.isupper()):
    print("the character is uppercase")
elif(char.islower()):
    print("the character is lowercase")
else:
     print("it's not an alphabet character.....")


#12. Write a Python program to input a number representing a day of the
#week (1 for Monday, 2 for Tuesday, etc.) and print the corresponding day.

day = int(input("Enter a day 1-7 :"))

if day == 1:
    print("monday",day)
elif day == 2:
    print("tuesday",day)
elif day == 3:
    print("wednesday",day)
elif day == 4:
    print("thurusday",day)
elif day == 5:
    print("friday",day)
elif day == 6:
    print("saturday",day)
elif day == 7:
    print("sunday",day)
else:
    print("invildle input!,please a enter between 1 to 7..")

 
#13. Write a Python program to input the month number (1 for January, 2 for
#February, etc.) and print the number of days in that month (considering
#leap years)

month = int(input("Enter a month number(1-12):"))

if month == 1:
    print("January : 31",month)
elif month == 2:
    print("February : 28",month)
elif month == 3:
    print("March : 31",month)
elif month == 4:
    print("April",month)
elif month == 5:
    print("May",month)
elif month == 6:
    print("June",month)
elif month == 7:
    print("July",month)
elif month == 8:
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


subj1 = float(input("Enter marks of subject1:"))

subj2 = float(input("Enter marks of subject2:"))

subj3 =float(input("Enter marks of subject3:"))

subj4 =float(input("Enter marks of subject4:"))

average =(subj1 + subj2 + subj3 + subj4) /4

if average >= 90:
    print("Grade A")
elif average >= 80:
    print("Grade B")
elif average >= 70:
    print("Grade C")
elif average >= 60:
    print("Grade D")
elif average >= 50:
    print("Grade E")
elif average < 50:
    print("Grade F")