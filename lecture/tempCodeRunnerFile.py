
def show(count):
   if(count == 0):    # base condition
      return
   print("Hello")
   show(count - 1)
show(10)

