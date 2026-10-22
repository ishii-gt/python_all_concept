# set  :store only unique value and mutable

l1 = [1,2,1,3,2,2321,231,2321,1,2]
t1 = (1,2,1,3,2,2321,231,2321,1,2)
s1 = {1,2,1,3,2,2321,231,2321,1,2}
print(l1)
print(t1)
print(s1)

for i in s1:
    print(i)



# add  : add(), update()
s1 = {1,2,3,4,5,6}

s1.add(7)
s1.add(7)
s1.add(7)
s1.add(7)
s1.add(7)
s1.update({12,12,7,89, 7, 123})
print(s1)

# delete : pop(), discard(value), clear()

s1 = {1,2,3,45,32,1,2,678}
print(s1)
s1.pop()
print(s1)
s1.discard(678)
print(s1)
s1.clear()
print(s1)


