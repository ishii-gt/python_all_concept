# string  : anything within inverted commas , immutable


s1 = "hello"

for i in s1:
    print(i)

print(s1[:])

# most : split , join , replace

s1 = "Firstname,Middlename,LaStname"

s1Update1 = s1.split(",")
# print(s1Update1[0] + "@company.domain")  # example
print(s1Update1)
s1Update2 = " | ".join(s1Update1)
print(s1Update2)
s1_cleaned = s1Update2.replace("LaStname","Lastname")
print(s1_cleaned)




#  upper(), lower(), captitallize(), title()

s1 = "hello world"
print(s1.upper()) 
print(s1.lower()) 
print(s1.capitalize()) 
print(s1.title()) 

# isalpha(), isdigit(), islaphnum(), startwith(), endwith()

s1 = "1"

print(s1.isalpha())
print(s1.isdigit())
print("1".isalnum())
print("hello".startswith("he"))
print("hello".endswith("h"))

s1 = "hello"

l1 = list(s1)
print(l1)