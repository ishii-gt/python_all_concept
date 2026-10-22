# exception : compile time exeception , run time exception 


# print("hello world")
# num = 


# num1 = 12
# num2 = 0
# print(num1 / num2)

# l1 = [1,2,3]
# print(l1[4])

# print("rest of the code....")

# f = open("data3.txt", "r")
# f.read()
# f.close()



# try :
#     num1 = int(input("Enter numerator : "))
#     num2 = int(input("Enter denomenator : "))
#     print("Ans :",num1 / num2)
#     l1 = [1,2,3]
#     # print(l1[4])
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except Exception as e:
#     print("error ho gayi ")

# else:
#     print("no error occure")
# finally :
#     print("risky code ended")

# print("rest of code....")

# manually raise error 

try:
    age = int(input("Enter your age : "))
    if(age < 18):
        # print("Child")
        raise Exception("You are not allowed")
    else:
        print("Adult")
except Exception as e:
    print(e)

print("rest of the code...")


# custom exception class  : (after oops )