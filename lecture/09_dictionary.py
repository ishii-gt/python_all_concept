# # dictionary  : key :value pair, mutable

# d1 = {
#     "id" :1,
#     "name" :"use1",
#     "salary" : 45000.45,
#     "address" : "nowhere"
# }

# print(d1)
# print(type(d1))


# print(d1["salary"])
# print(d1.get("salary"))
# # add : 

# d1["salary"] = 56000
# print(d1)
# d1["hobby"] = "timepass"
# print(d1)

# # delete

# del d1["hobby"]
# d1.pop("address")
# d1.popitem()
# print(d1)




# d1 = {
#     "id" :1,
#     "name" :"use1",
#     "salary" : 45000.45,
#     "address" : "nowhere"
# }

# keys = d1.keys()
# print(keys)

# values = d1.values()
# print(values)

# item = d1.items()
# print(item)




# dictionary  : {key : value}

info = {
    "id" : 1,
    "name" : "user1",
    "salary" : 45000,
    "address" : "nowhere"
}

print(info)
print(type(info))

print(info["salary"])




key = info.keys()

print(key)

for i in key:
    print(i, ":",info[i])

value = info.values()
print(value)

item = info.items()
print(item)

# add
info["hobby"] = "coding"
print(info)

# delete  , pop(key), popitem(), clear()

info.pop("id")
print(info)

info.popitem()
print(info)

info.clear()
print(info)