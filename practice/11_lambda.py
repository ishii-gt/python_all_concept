#Basic:

#1. Write a lambda function to find the cube of a number.

cube = lambda x: x**3
num=int(input("Enter character:"))
print("cube =",cube(num))

#2. Write a lambda function to calculate the square of a number.

square = lambda x: x**2
num1 =int(input("Enter character:"))
print("square =",square(num1))


#3. Write a lambda function to check if a number is even.

even = lambda x: x % 2 == 0

num =int(input("Enter a number:"))
if even(num):
    print("even number")
else:
    print("not a even number")

#4. Write a lambda function to check if a number is a prime number.

prime = lambda n :n>1 and all(n % i !=0 for i in range(2,n))
num = int(input("Enter a number:"))
if prime(num):
    print("prime number")
else:
    print("not prime number")

#5. Write a lambda function to reverse a string.


reverse = lambda x :x[::-1]

text =input("Enter a string:")
print("reverse string:",reverse(text))

#6. Write a lambda function to convert a Celsius temperature to Fahrenheit.

fahrenheit =lambda c:(c* 9/5)+32

celsius=float(input("Enter temperature in celsius :"))
print("celsius temperature to fahrenheit:",fahrenheit(celsius))


#Sorting and Filtering:


# 1. Use lambda with sorted() to sort a list of integers in descending order.

l1=[1,2 ,56,3,-75,0,-3345,9337]
l1.sort()
print(l1)

l2= sorted(l1)
print(l2)

#2. Use lambda with filter() to filter a list of integers to get only even numbers.


l1 = [ 1,2,3,4,5,6]

evenNumber = list(filter(lambda x : x % 2 == 0, l1))
print(evenNumber)


#3. Use lambda with map() to convert a list of Celsius temperatures to Fahrenheit.

l1 = [1,2,3,4,5]



squareL1 = list(map(lambda x : x**2, l1))
print(squareL1)



fahrenheit =lambda c:(c* 9/5)+32

celsius=float(input("Enter temperature in celsius :"))
print("celsius temperature to fahrenheit:",fahrenheit(celsius))



#Functional Programming Concepts:
#1. Write a lambda function to find the factorial of a number using recursion.

factorial =lambda n:1 if n==0 or n==1 else n* factorial(n-1)
num=int(input("Enter a number:"))
print("Factorial number",factorial(num))


#2. Write a lambda function to implement the Fibonacci sequence up to n terms.


#fibonacci =lambda n:[] if n==0 else[0]if n==1 else [0,1]
#num = int(input("Enter a number:"))
#print("fibonacci sequence"fibonacci(num))
