# abstraction  : hide your implementation


from abc import ABC, abstractmethod


class Rbi(ABC):
    @abstractmethod # decorator
    def interestRate(self):
        pass
    @abstractmethod
    def loan(slef):
        pass

    def display(self):   # concrete method
        print("i'm rbi")


class BOB(Rbi):
    def interestRate(self):
        print("8.9")
    def loan(slef):
        print("Loan")
    def display(self):
        super().display()
        print("I'm BOB")

bob = BOB()
bob.display()

# rbi = Rbi()   cannot instantiate abstract class



