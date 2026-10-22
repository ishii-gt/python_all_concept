#Creating and Accessing Dictionaries:

#1. Write a Python program to create a dictionary with key-value pairs
#representing the names of students and their grades. Print the grade of a
#specific student.

student = {
    "ishi" :"A",
    "pari" :"B",
    "prem" :"C",
    "harsh":"D",
    "ashish":"E",
}

keys = student.keys()
print(keys)

values = student.values()
print(values)

print("Enter a grade:",student)

#2. Given a dictionary, write a Python function to add a new key-value pair
#to it. Also, demonstrate how to update the value of an existing key.



#Dictionary Methods:
#3. Write a Python program to demonstrate the use of the get() method for retrieving values from a dictionary.

student = {
    "ishi":"A",
    "ajay": "B",
    "pari" :"A+",

}
print("Grade of ajay:",student.get("ajay"))


#4. Write a Python program to demonstrate the use of the items(), keys(), and values() methods to iterate over a dictionary's keys and values.




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

item = d1.items()
print(item)

#Removing Elements:
#5. Write a Python program to remove a specific key-value pair from dictionary using the pop() method. Also, demonstrate the use of the
#popitem() method to remove and return the last inserted key-value pair.


d1 = {
    "id" :1,
    "name" :"use1",
    "salary" : 45000.45,
    "address" : "nowhere"
}

print(d1)
print(type(d1))


print(d1["salary"])
print(d1.get("salary"))
# add : 

d1["salary"] = 56000
print(d1)
d1["hobby"] = "timepass"
print(d1)

# delete

del d1["hobby"]
d1.pop("address")
d1.popitem()
print(d1)

#Checking Existence of Keys:
#6. Write a Python function that checks whether a given key exists in a dictionary and returns an appropriate message.

