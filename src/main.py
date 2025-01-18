import logging
    
class BankAccountError(Exception):
    """Base class for exceptions in the bank account module"""
    pass

class NegativeAmountError(BankAccountError):
    """Exception raised for negative error"""
    pass

class InsufficientFundsError(BankAccountError):
    """Exception raised when trying to withdraw more than the balance"""
    pass
    
class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0) -> None:
        self.account_holder = account_holder
        self._balance = balance
        
    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise NegativeAmountError("Deposit amount must be positive")
        self._balance += amount
        logging.info("Deposit {}. New balance {}".format(amount, self.balance))
        
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive")
        elif amount > self.balance:
            raise InsufficientFundsError("Insufficient Funds")
        self._balance -= amount
        logging.info(f"Withdraw: {amount}. New balance: {self.balance}")
        
    def __str__(self) -> float:
        return f"Account holder: {self.account_holder}, Balance: {self.balance}"
    