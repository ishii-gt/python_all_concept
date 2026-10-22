# list : store mulitple value in a single container of different dataType , mutable

l1 = []
print(l1)
print(type(l1))

l1 = [12, 13.4, "name", True]
print(l1)
# print(l1[0])
# print(l1[1])
# print(l1[2])
# print(l1[3])

# print(len(l1))

for i in range(len(l1)):
    print(i, l1[i])

for i in l1:
    print(i)


# add : append(Value), insert(index, value), extend([])


l1 = [1,2,3,4,5,6]
print(l1)
l1.append(7)
print(l1)
l1.insert(3, 3.5)
print(l1)
l2 = [8,9,10,11]
l1.extend(l2)
print(l1)

# deleting : pop(), pop(index), remove(value), clear()

l1 = [1,2,3,4,5]
print(l1)
l1.pop()
print(l1)
l1.pop(1)
print(l1)
l1.remove(4)
print(l1)
l1.clear()
print(l1)


# special function : sort(), reverse(), copy()

l1 = [ 34, -123 , 9 , 0 , 4534]
# l1.sort()
# print(l1)
l1.sort(reverse=True)
print(l1)

l1 = [ 23 , 45 , 89 , 0 , 23 , -1]
l1.reverse()
print(l1)


l1 = [ 12, 34]
l2 = l1      # pass by reference
l2.append(55)
print(l1)
print(l2)


l1 = [12,34]
l2 = l1.copy()
l2.append(55)
print(l1)
print(l2)


# slicing  : index

l1 = [10, 11, 12, 13, 14, 15, 16, 17]
print("1 :", l1)
print("2 :", l1[:])
print("3 :", l1[2:])
print("3 :", l1[2:4])
print("4 :", l1[::1])
print("5 :", l1[::2])
print("5 :", l1[::-1])
print("5 :", l1[5:1:-1])


# list comprehension : 


# l1 = []

# for i in range(1,101):
#     l1.append(i)

# print(l1)

l1 = [i for i in range(1, 101)]
print(l1)
l1 = [i**2 for i in range(1, 101)]
print(l1)
l1 = [i for i in range(1, 101) if i % 2 == 0]
print(l1)

