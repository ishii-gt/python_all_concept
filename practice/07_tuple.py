#Basic Tuple Operations:
#1. Write a Python program to create a tuple with different data types.

t1=(12,34.54,"name",True)
print(t1)

#2. Write a Python program to create a tuple and find the length of the tuple.

t1=(1,2,3,4,5,6)
length =len(t1)
print("tuple",t1)
print("length of tuple:",length)

#Tuple Indexing and Slicing:
#3. Write a Python program to access an element in a tuple using indexing.

t=(10,20,30,40,50,60,70)
print("First element:",t[0])
print("Secode element:",t[4])

#4. Write a Python program to slice a tuple from index 2 to 5.
t =(10,20,30,40,50,60)

slice_tuple = t[2:5]
print("slice a tuple:",slice_tuple)


#Tuple Concatenation and Repetition:
#5. Write a Python program to concatenate two tuples.

t1=(1,2,3)
t2=(4,5,6)

result = t1 + t2
print("concatenate tuple:",result)

#6. Write a Python program to repeat a tuple 3 times.

t1 = (1,2,3)
result = t1*3
print("repeat tuple:",result)

#Tuple Unpacking:
#7. Write a Python program to unpack a tuple into several variables.

t = ("ishi",20,"surat")
name,age,city =t

print("Name:",name)
print("Age:",age)
print("City:",city)


#8. Write a Python program to swap two variables using tuple unpacking.

t1 = (3.14, 9.8)
pie , g = t1
print(pie)
print(g)

#Nested Tuples:
#9. Write a Python program to access elements of a nested tuple.

t=(1,2(3,4,5),6)
print("Enter first",t[0])
print("Enter second",t[2])
print("Etnter a nested tuple:",t[2][1])

#10.Write a Python program to change an element in a nested tuple
#(considering tuples are immutable, use a workaround).



#Tuple Methods and Functions:
#11. Write a Python program to find the index of a specific element in a tuple.

t1 = (1,2,1,1,2,1,2,1)
#print(t1.count(1))
print(t1.index(2))


#12.Write a Python program to count the occurrences of a specific element in a tuple.


t1 = (1,2,1,1,2,1,2,1)
print(t1.count(1))
#print(t1.index(2))

#Tuple Comprehensions and Conversions:
#13. Write a Python program to convert a tuple to a string.

t =('h','e','l','l','o')
result =''.join(t)
print("convert a tuple:",result)

#14.Write a Python program to convert a list to a tuple and vice versa.

l1=[1,2,3]
t1=tuple(l1)

print("tuple:",l1)

t2=[4,5,6,7,8]
l2=list(t2)

print("list:",t2)

#Advanced Tuple Operations:
#15. Write a Python program to sort a tuple of numbers.

t = ( 34, -123 , 9 , 0 , 4534)
sort_tuple =tuple(t)
print("Sort a tuple:",sort_tuple)

#16.Write a Python program to sort a list of tuples based on the second element.

#l =([1,4],[2,3],[4,5],[4,1],[6,1])
#sort_list = sortlist(l,key=lambda x:x[l])
#print("sorted list",sortlist)


#Tuple in Functions:
#17. Write a Python program to return multiple values from a function using tuples.

def info(*argus):
      return argus

print(info(1,2,3,4,5,6))


#18.Write a Python program to pass a tuple as an argument to a function.

def show_tuple(t):
    for i in t:
     
            print(i)
t=(10,20,30,40,50)
show_tuple(t)

#Tuple as Dictionary Keys:
#19. Write a Python program to use a tuple as a key in a dictionary.




d1 = {
    "id" :1,
    "name" :"use1",
    "salary" : 45000.45,
    "address" : "nowhere"
}

keys = d1.keys()
print(keys)


# 20.Write a Python program to iterate over dictionary items where keys are tuples.


d1 = {
    "id" :1,
    "name" :"use1",
    "salary" : 45000.45,
    "address" : "nowhere"
}

keys = d1.keys()
print(keys)

values = d1.values()
print(values)


#Tuple Exercises with Algorithms:
#21. Write a Python program to find the second largest element in a tuple.




#22.Write a Python program to merge two sorted tuples into one sorted tuple.




#Real-world Scenario:
#23. Write a Python program to store student records (name, age, grade) in a
#tuple and perform CRUD (Create, Read, Update, Delete) operations.

data = ()

def add(adata):
    print(adata)
    name = input("Enter your name : ")
    age = int(input("Enter your age: "))
    grade = input("Enter your grade: ")
    adata += ((name,age,grade),)
    return adata

def update(udata):
    for i in range(len(udata)):
        print(i , ":", udata[i])
    index = int(input("Enter index that to be change : "))
    print(udata[index])
    innerIndex = int(input("Enter inner index : ")) 
    value = input("Enter value to be change : ") 
    item = list(udata[index])
    item[innerIndex] = value
    item = tuple(item)
    udata = list(udata)
    udata[index] = item
    udata = tuple(udata)
    return udata

def delet(ddata):
    if len(ddata)==0:
      print("No recode found.")
      return ddata
    
    for i in range(len(ddata)):
         print(i,":",ddata[i])

    index =int(input("Enter index to delete :"))  
    ddata = list(ddata)
    ddata.pop(index)
    ddata = tuple(ddata)
    return ddata


# ((1,"name"),(2, "name2"))
# (2, "name2") -> [2, "name2"] -> [2,"name24"] -> (2,"name24") :: [(1,"name"),(2, "name2")], [(1,"name"), (2,"name24")] -> ((1,"name"), (2,"name24"))

def show(sdata):
    for i in sdata:
        print("-"*15)
        print(i)      
        # print("-"*15)



while(True):
    print("Enter 1 for Add Data\nEnter 2 for Show Data\nEnter 3 for Delete Data\nEnter 4 fro Update Data\nEnter 5 for Exit : ")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        data = add(data)
    elif(choice == 2):
        show(data)
    elif(choice == 3):
      data = delet(data)

    elif(choice == 4):
        data = update(data)
    elif(choice == 5):
        print("System closed!!!")
        break  
    else:
        print("Give proper input")