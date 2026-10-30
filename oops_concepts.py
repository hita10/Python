from abc import ABC, abstractmethod

# Abstraction and Encapsulation
class BankAccount(ABC):
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    @abstractmethod
    def calculate_interest(self) -> float:
        pass


# Inheritance and Polymorphism
class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float, interest_rate: float):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self) -> float:
        interest = self.get_balance() * self.interest_rate
        print(f"Calculated Interest for {self.owner}: ${interest}")
        return interest


class CheckingAccount(BankAccount):
    def __init__(self, owner: str, balance: float, fee: float):
        super().__init__(owner, balance)
        self.fee = fee

    def calculate_interest(self) -> float:
        print("Checking accounts do not earn interest.")
        return 0.0


# Execution
savings = SavingsAccount("Alice", 1000.0, 0.05)
savings.deposit(500.0)
savings.calculate_interest()

checking = CheckingAccount("Bob", 500.0, 12.0)
checking.calculate_interest()
