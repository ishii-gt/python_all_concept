
class Book:
    def __init__(self, title, author, stock):
        self.title = title
        self.author = author
        self.__stock = stock

    def add_stock(self, quantity):
        self.__stock += quantity

    def sell_book(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            print(quantity, "book(s) sold")
        else:
            print("Not enough stock")

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Stock:", self.__stock)


b1 = Book("Python Programming", "John", 20)

b1.display_details()
b1.add_stock(10)
b1.sell_book(5)
b1.display_details()