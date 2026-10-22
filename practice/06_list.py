#Basic List Operations
#1. Write a Python program to create a list of 10 integers and print the list.

number = [1,2,3,4,5,6,7,8,9,10]

print("Enter a 10 integers:",number)

#2. Write a Python program to append an element to a list.


l1 = [1,2,3,4,5,6]
print(l1)
l1.append(7)
print(l1)

#3. Write a Python program to insert an element at a specific position in a
#list.

l1 =[10,20,30,40,50]
print(l1)
l1.insert(2,3.1)
print(l1)

#4. Write a Python program to remove an element from a list.

l1 =[10,20,30,40,50,60,70]
print(l1)
l1.remove(40)
print(l1)


#List Slicing
#5. Write a Python program to print the first 5 elements of a list.

l1 =[1,2,3,4,5]
print(l1)

#6. Write a Python program to print the last 5 elements of a list.

l1 =[10,20,30,40,50,60,70,80,90,100]
print(l1)
print(l1[5:])

#7. Write a Python program to print a sublist from index 2 to index 7.

l1 =[10,20,30,40,50,60,70,80,90,10]
print(l1)
print (l1[2:7])

#List Comprehensions
#8. Write a Python program to create a list of squares of numbers from 1 to 10 using list comprehension.

l1 = [i**2 for i in range(1, 11)]
print(l1)

#9. Write a Python program to create a list of even numbers from 1 to 20
#using list comprehension.


l1 = [i for i in range(1, 21) if i % 2 == 0]
print(l1)

#Advanced List Operations
#10. Write a Python program to find the maximum and minimum elements in a list.

l1 =[5,10,15,22,20,25,30]

maximum =max(l1)
minimum =min(l1)

print("maximum element:",maximum)
print("minimum element:",minimum)

#11. Write a Python program to find the sum of all elements in a list.

l1=[12 + 34]
print(l1)

#12. Write a Python program to count the number of occurrences of a specific element in a list.

list = [10.20,30,40,50,50,50]
print(list)

element = 50
count = 0

for i in list:
    if i == element:
        count += 1
print(count)



#List Methods
#13. Write a Python program to sort a list in ascending and descending order.

l1=[54, 9124, 0, -34 ,3456]
l1.sort()
print(l1)

#14. Write a Python program to reverse a list.

l1=[54, 9124, 0, -34 ,3456]
l1.reverse()
print(l1)

#15. Write a Python program to find the index of a specific element in a list.


list = [10,20,30,40,50]
print(list)
element = int(input("Enter the element : "))
print(list.index(element))


#List Transformation
#16. Write a Python program to convert a list of strings to a list of integers.

l1 =["1","2","3","4","5","6","7"]
print(l1)
lnew =[]
for i in l1:
    lnew.append(int(i))
print(lnew)

#17. Write a Python program to convert a list of lists into a single list.

l1=[["1","2"],["3","4"],["5","6"]]
print(l1)
lnew = []
for i in l1:
    for j in i:
      lnew.append(int(j))
print(lnew)

#Nested Lists
#18. Write a Python program to create a 3x3 matrix as a nested list.


# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# 00, 01, 02
# 10, 11, 12,
# 20 , 21, 22



lrow = []

for r in range(3):
    lcol = []
    for c in range(3):
        element = int(input(f"Enter an element ({r} , {c}) : "))
        lcol.append(element)
    lrow.append(lcol)
for i in lrow:
    print(i)

for r in range(3):
    for c in range(3):
        print(lrow[c][r], end=" ")
    print()






# 20. Write a Python program to iterate over a list and print each element.

list = [10, 20, 30, 40, 50]

for i in list:
    print(i)



# 21. Write a Python program to iterate over a list and print only the even 
# elements.


list = [10,20,33,55,24,63,100,73]

for i in list:
    # print(i)
    if i % 2 == 0:
        print(i)

#List Combinations
#22. Write a Python program to find all possible pairs of elements in a list.

# l1 = [1 ,2,3,1,3,2]
# lnew = [[1,1], [2,2], [3,3]]

l1=[1,2,3,4,5]

for i in range(len(l1)):
 for j in range(i+1,len(l1)):
     print(l1[i],l1[j])
 




#23. Write a Python program to generate all possible combinations of
#elements from two lists.

l1=[1,2,3]
l2=[4,5,6]

for i in l1:
 for j in l2:
     print([i,j])


#List Filtering
# 24. Write a Python program to filter out all odd numbers from a list. 


 list = [1,2,3,4,5,6,7,8,9]
even = []
for i in list:
    if i % 2 == 0:
        even.append(i)

print(even)


# 25. Write a Python program to filter out all numbers greater than a specific 
# value from a list. 
l1 = [ 12, 34, 0 , 89]

specific = 12
for i in l1:
    if(i > specific):
        print(i)