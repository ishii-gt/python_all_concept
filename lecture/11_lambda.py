# lambda function 

# def square(num):
#     return num**2

# print(square(8))


# lambda  : 

square = lambda num : num**2

print(square(8))



# map , filter

# map : if i want to apply a same logic on each element  map length = actuall length

l1 = [1,2,3,4,5]



squareL1 = list(map(lambda x : x**2, l1))
print(squareL1)


# filter: it filter out the stuff  filter length <= actuall length


l1 = [ 1,2,3,4,5,6]

evenNumber = list(filter(lambda x : x % 2 == 0, l1))
print(evenNumber)


l1 = [1,2,3,3,4,6]
leven = list(filter(lambda x : x % 2 == 0, l1))
lfinal = list(map(lambda x : x **2, leven))
print(lfinal)

l2 = sum(l1)
print(l2)


# list  : sort(), sorted()

l1 = [1,2,34,-9, 0 , -99]
# l1.sort()
print(l1)

l2 = sorted(l1)
print(l1)
print(l2)


l1 = [ "Anujal","Anuj", "Anu", "Anuja",]

l2  = sorted(l1 , key = len)
print(l2)


# bubble sort 
# l1 = [ "Anujal","Anuj", "Anu", "Anuja",]

# for i in l1:


from functools import reduce


l1 = [ 1,2,3,4,5]
# x : 1, 3, 6, 10, 15
# y :2, 3, 4, 5

ans = reduce(lambda x, y: x+ y, l1)
print(ans)




row = int(input("Enter "))
