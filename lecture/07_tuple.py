# tuple : store muliptle value in a single container of different type but they are immutable

t1 = (1,2,3,4,5,"string",True, 56.45)
print(t1)
print(type(t1))


t1 = (1,)
print(t1)
print(type(t1))


t1 = (1,2,3,4,5,6)
for i in t1:
    print(i)

print(t1[2])

print(t1[:])


l1 = list(t1)
print(l1)


# unpacking  
t1 = (3.14, 9.8)
pie , g = t1
print(pie)
print(g)
# swapping 
pie , g = g , pie
print(pie)
print(g)



# count(), index()

t1 = (1,2,1,1,2,1,2,1)
print(t1.count(1))
print(t1.index(2))


# tuple comprehension:

t1 = (i for i in range(1 , 101))
print(tuple(t1))

