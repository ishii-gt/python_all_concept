# loop : repeatation of a block of code

# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")

# 1,2,3,4,5,6......100

# for , while
# for : start and ending known
# syntax :
# for variableName in range():
#     execute
# range(starting Point(default = 0),ending Point(excluded), stepping(default = 1, inc/dec))

for i in range(1,5, 2):
    print(i)
else:
    print("Loop ended")

for i in range(10, 0, -1):
    print(i)
else:
    print("Loop ended")



# when you only know about starting

i = 1
while(i <= 10):
    print(i)
    i += 1

i = 10
while(i >= 1):
    print(i)
    i -= 1

#1. Write a Python program to print all natural numbers from 1 to n
#using a while loop.

n = int(input("Enter a number:"))
i = 1
while(i <= n):
    print(i)
    i+=1
#2. Write a Python program to print all natural numbers in reverse order
#from n to 1 using a while loop.

n = int(input("Enter a number : "))
i = 10
while(i>=n):
    print(i)
    i-=1
#3. Write a Python program to print all alphabets from 'a' to 'z' using a
#while loop.

# a -> 97, 98  :10010111  z -> 122
# A -> 65 , 66           Z -> 90
# 32 , b - B : 32
print(ord("a"))  # charactor to number
print(chr(121))  # number to charactor


start = input("Starting : ")
end = input("Ending : ")

while(start <= end):
    print(start, ord(start), chr(ord(start) - 32), ord(start) - 32)
    start = chr(ord(start) + 1)


#4. Write a Python program to print all even numbers between 1 to 100
#using a while loop.

start = int(input("Enter starting number :"))
end = int(input("Enter ending number :"))
while start <= end:
    if(start % 2 == 0):
        print(start)
    start += 1

#5. Write a Python program to print all odd numbers between 1 to 100
#using a while loop.

start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))
while start <= end:
    if(start % 2 == 1):
        print(start)
    start +=1

#6. Write a Python program to find the sum of all natural numbers
#between 1 to n using a while loop.
#  1 to 5 : 1 + 2 + 3 + 4 + 5 = 15
start = int(input("Enter starting point :"))
end = int(input("Enter ending point :"))
sum = 0

while start <= end:
    sum = sum + start
    start += 1

print(sum)
#7. Write a Python program to find the sum of all even numbers between
#1 to n using a while loop.

n = int(input("Enter the sum of even number between 1 to n: "))

num =2
total = 0

while num <=n:
    total =total +num
    num +=2
    print("sum to even",total)

#8. Write a Python program to find the sum of all odd numbers between
#1 to n using a while loop.

n =int(input("Enter the sum of odd number between 1 to n:"))

num = 1
total  = 0

while num <= n:
    total = total +num
    num +=2
    print("sum to odd ",total)

#9. Write a Python program to print the multiplication table of any
#number using a while loop.

num=int(input("Enter multiplication table:"))

i=1
while i<=10 :
    print(num,"x",i,"=",num*i)
    i+=1

#10. Write a Python program to count the number of digits in a
#given number using a while loop.

num = int(input("Enter a Number:"))

count = 0
while num != 0:
   num = num // 10

  
   count +=1
print(count)

# num = 1234
# print(num % 10)

# 1234 // 10 : 123 // 10 : 12 // 10 : 1 // 10 : 0
# print(num // 10)


#11. Write a Python program to find the first and last digit of a
#number using a while loop.

num = int(input("Enter a Number:"))
first_digit=num
last_digit = num % 10
if(num==0):
    print("First and last digit are",0)
else:
    while first_digit >= 10: #1234
        first_digit = first_digit //10


print("First digit",first_digit)
print("Last digit",last_digit)

#12. Write a Python program to find the sum of the first and last
#digit of a number using a while loop.








# nested Loop  : 


# *****
# *****
# *****
# *****
# *****
# Square Star Pattern



row = int(input("Enter row count : "))
col = int(input("Enter col count : "))

for r in range(1 , row + 1):
    for c in range(1 , col + 1):
        print("*", end="")
    print()


# *****
# *   *
# *   *
# *   *
# *****
# Hollow Square Star
# Pattern



row = int(input("Enter row count : "))
col = int(input("Enter col count : "))

for r in range(1 , row + 1):
    for c in range(1 , col + 1):
        if(r == 1 or c == 1 or r == row or c == col or  r == col or c == row +1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


#*****
#** **
#* * *
#** **
#*****
#Hollow Square Star
#Pattern with Diagonal



row =int(input("Enter row count:"))
col =int(input("Enter col count:"))

for r in range(1, row + 1):
    for c in range(1, col + 1):
        if(r == 1 or c == 1 or r == row or c == col or r == col or r == c):
             print("*",end="")
        else:
            print("",end="")
        print()



#    *****
#   *****
#  *****
# *****
# *****
#Rhombus Star Pattern


row=int(input("Enter row count:"))
col=int(input("Enter col count:"))

for r in range(1 , row+1):
    for c in range(1, col + 1):
        if(r == 1 or c == 1 or c== row or r == col or col == col ):
         print("*",end="")
        else:
            print(" ",end="")
    print()




# *
# **
# ***
# ****
# *****
# Right Triangle
# Star Pattern



row = int(input("Enter number of rows : "))

for r in range(1 , row + 1):
    for c in range( 1 , r + 1):
        print("*", end="")
    print()



# *****
# ****
# ***
# **
# *
# Inverted Right Triangle
# Star Pattern


row = int(input("Enter number of rows :"))

for r in range(1, row + 1):
    for c in range(row - r + 1, 0, - 1):
        print("*", end="")
    print()





#    *****
#   *****
#  *****
# *****
#*****
#Rhombus Star Pattern

row =int(input("Enter row count:"))
col =int(input("Enter col count:"))

for r in range(1, row +1):
    for c in range(row - r + 1, 0, - 1):
        print(" ", end="")
    
    for c in range(1, col +1):
        print("*",end="")
    print()


#   *****
#  *    *
# *    *
#*    *
#*****
#Hollow Rhombus Star
#Pattern

row = int(input("Enter row count : "))
col = int(input("Enter col count : "))

for r in range(1 , row + 1):
    for c in range(row - r + 1, 0, - 1):
        print(" ", end="")
    for c in range(1 , col + 1):
        if(r == 1 or c == 1 or r == row or c == col or  r == col or c == row +1):
            print("*", end="")
        else:
            print(" ", end="")
    print()



#*****
# *****
#  *****
#   *****
#    *****
#Mirrored Rhombus Star
#Pattern



row =int(input("Enter row count:"))
col =int(input("Enter col count:"))

for r in range(1, row +1):
     for c in range( 1 , r + 1):
        print(" ", end="")
     for c in range(1, col +1):
        print("*",end="")
     print()



 
#*****
# *   *
#  *   *
#   *   *
#    *****
#Hollow Mirrored
#Rhombus Star Pattern


row = int(input("Enter row count : "))
col = int(input("Enter col count : "))

for r in range(1 , row + 1):
     for c in range( 1 , r + 1):
        print(" ", end="")
     for c in range(1 , col + 1):
        if(r == 1 or c == 1 or r == row or c == col or  r == col or c == row +1):
            print("*", end="")
        else:
            print(" ", end="")
     print()




#*
#**
#*  *
#*   *
# *****
#Hollow Right Triangle
#Star Pattern



row = int(input("Enter number of rows : "))

for r in range(1 , row + 1):
    for c in range( 1 , r + 1):
        if(r == row or c == 1 or r == c):
            print("*", end="")
        else:
            print(" ", end="")
    print()

 #   *
 #  **
 # ***
 #****
#*****
#Mirrored Right Triangle
#Star Pattern



row =int(input("Enter row count:"))
col =int(input("Enter col count:"))

for r in range(1, row +1):
    for c in range(row - r + 1, 0, - 1):
        print(" ", end="")
    for c in range( 1 , r + 1):
        print("*", end="")
    print()



    # *
   # **
  # *  *
 # *  *
# *****
#Hollow Mirrored Right
#Triangle Star Pattern





row =int(input("Enter row count:"))
col =int(input("Enter col count:"))

for r in range(1, row +1):
    for c in range(row - r + 1, 0, - 1):
        print(" ", end="")
    for c in range( 1 , r + 1):
        print("*", end="")
    print()



#11111
#11111
#11111
#11111
#11111
#Number pattern 1


row = int(input("Enter row count : "))
col = int(input("Enter col count : "))

for r in range(1 , row + 1):
    for c in range(1 , col + 1):
        print("1", end="")
    print()


#11111
#00000
#11111
#00000
#11111
#Number pattern 2

row = int(input("Enter row count : "))
col = int(input("Enter col count : "))

for r in range(1 , row + 1):
    for c in range(1 , col + 1):
        if(r % 2 == 0):
          print("0", end="")
        else:
            print("1",end="")
    print()


#01010
#01010
#01010
#01010
#01010
#Number pattern 3

row =int(input("Enter row count:"))
col =int(input("Enter col count:"))


for r in range(1 , row + 1):
    for c in range(1 , col + 1):
        if(c % 2 == 0):
          print("1", end="")
        else:
            print("0",end="")
    print()

#11111
#10001
#10001
#10001
#11111
#Number pattern 4



row = int(input("Enter row count : "))
col = int(input("Enter col count : "))

for r in range(1 , row + 1):
    for c in range(1 , col + 1):
        if(r == 1 or c == 1 or r == row or c == col or  r == col or c == row +1):
            print("1", end="")
        else:
            print("0", end="")
    print()

#11011
#11011
#00000
#11011
#11011
#Number pattern 7



row = int(input("Enter row count : "))
col = int(input("Enter col count : "))

for r in range(row):
    for c in range(row):
        if(r == 2 or c == 2 ):
            print("0", end="")
        else:
            print("1", end="")
    print()



#11111
#22222
#33333
#44444
#55555
#Number pattern 10

row = int(input("Enter row count:"))
col = int(input("Enter col count:"))

for r in range(1,row+1):
    print(str(r)*5)


#12345
#12345
#12345
#12345
#12345
#Number pattern 11

row = int(input("Enter row count:"))
col = int(input("Enter col count:"))

for r in range(row):
    for c in range(1,col + 1):
        print(c,end="")
    print()


#12345
#23456
#34567
#45678
#56789
#Number pattern 12

row =int(input("Enter row count:"))
col =int(input("Enter col count:"))

for r in range(1,row + 1):
    for c in range(r,r+row):
        print(c,end="")
    print()

#12345
#21234
#32123
#43212
#54321
#Number pattern 17
# row =int(input("Enter row count:"))
# num =int(input("Enter num count:"))
 

# for r in range(row):
#   for num in range(r, r+row):
#       print(num,end="")
#       num += 1
#   print()