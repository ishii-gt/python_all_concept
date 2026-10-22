#loop : block of code

#1. Write a Python program to print all natural numbers from 1 to n
#using a while loop.

n = int(input("Enter a number:"))

i=1
while(i <= n):
    print(i)
    i+=1

#2. Write a Python program to print all natural numbers in reverse order
#from n to 1 using a while loop.

n = int(input("Enter a number:"))

i=10
while(i >= n):
    print(i)
    i-=1

#3. Write a Python program to print all alphabets from 'a' to 'z' using a
#while loop.

# a: 97 , 98 and z =122
#A : 65 ,66 and Z = 90

print(ord("a")) #charactor to number
print(chr(122)) #number to charactor


start = input("Starting : ")
end = input("Ending : ")

while(start <= end):
    print(start, ord(start), chr(ord(start) - 32), ord(start) - 32)
    start = chr(ord(start) + 1)


#4. Write a Python program to print all even numbers between 1 to 100
#using a while loop.

start = int(input("Enter a starting:"))
end  = int(input("Enter a Ending :"))

while start <= end:
    if(start % 2 == 0):
        print(start)
    start +=1  


#5. Write a Python program to print all odd numbers between 1 to 100
#using a while loop.

start = int(input("Enter a string:"))
end = int(input("Enter a Ending:"))

while start <= end:
    if(start % 2 == 1):
        print(start)
    start +=1


#6. Write a Python program to find the sum of all natural numbers
#between 1 to n using a while loop.

start = int(input("Enter a string:"))
end  = int(input("Enter a Ending:"))

sum=0
while start <= end:
    sum = sum + start
    start +=1
print(sum)

#7. Write a Python program to find the sum of all even numbers between
#1 to n using a while loop.

n = int(input("Enter the sum of even numbers between 1 to n:"))

num = 2
total = 0

while num <= n:
   total = total + num
   num +=2
   print("sum to even" ,total)


#8. Write a Python program to find the sum of all odd numbers between
#1 to n using a while loop.


n = int(input("Enter the sum of odd numbers between 1 to n :"))

num =2
total = 0

while num <=n:
    total = total + num
    num += 1
    print("sum of odd ",total)


#9. Write a Python program to print the multiplication table of any
#number using a while loop.

num =int(input("Enter the multiplication table:"))

i=1
while i<=10:
    print(num ="x")









#nested Loop


#*****
#*****
#*****
#*****
#*****
#Square Star Pattern


row =int(input("Enter row count:"))
col =int(input("Enter col count:"))

for r in range(1, row +1):
    for c in range(1, col +1):
        print("*",end="")
    print()

#*****
#** **
#* * *
#** **
#*****
#Hollow Square Star
#Pattern with Diagonal

row = int(input("Enter row count:"))
col = int(input("Enter col count:"))

for r in range(1, row + 1):
    for c in range(1, col +1):
      if(r == 1 or c == 1 or r == row or c == col or r == col  or  r == c  ):
        print("*",end="")
      else:
            print(" ",end="")
    print()

#*****
#*   *
#*   *
#*   *
#*****
#Hollow Square Star
#Pattern


row = int(input("Enter row count : "))
col = int(input("Enter col count : "))

for r in range(1 , row + 1):
    for c in range(1 , col + 1):
        if(r == 1 or c == 1 or r == row or c == col or  r == col or c == row +1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


#  *****
#  *****
# *****
#*****
#*****
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


#  *****
# *    *
# *    *
#*   *
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

    