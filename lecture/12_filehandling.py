# file Handling : To handle our file
# mode  : w(write and create file if not exist ) ,
#  r(read existed file),
# a(append file(update)), 
# +w(write and read) , 
# +r(read and write) , 
# +a(append and read)

# f = open("data.txt", "w")
# f.write("hello world 1\n")
# f.writelines(["hello world 2\n", "hello world3\n", "hello world4\n"])
# f.close()

# with open("data.txt", "r") as f:
#     # data = f.read()
#     # data = f.readline()
#     data = f.readlines()
#     print(data[2])

# with open("data.txt", "a") as f:
#     f.write("\nWelcome back")


# with open("data2.txt", "+w") as f:
#     f.write("hello world")
#     place = f.tell()
#     print(place)
#     f.seek(0)
#     data = f.read()
#     print(data)



# with open("data.txt", "w") as f:
#     f.write("hello world1")
#     f.writelines(["\nhello world2", "\nhello world3", "\nhello world4"])


# with open("data.txt", "r") as f:
#     data = f.read()
#     print(data)


# with open("data.txt", "a") as f:
#     f.write("\nhello world5")



with open("data.txt", "+a") as f:
    # f.write("\nhello world6")
    f.seek(0)
    data = f.read()
    print(data)