# Bank Application with Unit Testing  

## Project Overview  
This project is a Python-based bank account application with robust unit testing. The application includes essential features such as deposits, withdrawals, and exception handling for invalid transactions. It is designed to demonstrate clean coding practices and test-driven development using Python's `unittest` module.  

---

## Features  
- **Deposit Funds:** Allows users to deposit money into their accounts with validation for positive amounts.  
- **Withdraw Funds:** Enables withdrawals while handling cases like insufficient funds and negative amounts.  
- **Balance Inquiry:** Provides the current balance in a secure and encapsulated manner using a property method.  
- **Custom Exceptions:** Implements specific error classes for precise exception handling:
  - `NegativeAmountError`: Raised for negative deposit/withdrawal amounts.  
  - `InsufficientFundsError`: Raised when attempting to withdraw more than the available balance.  

---

## Project Structure  
The project is organized as follows:  

bank-app/ │ ├── src/ │ └── main.py 
# Contains the BankAccount class and custom exceptions. │ ├── tests/ │ └── testfile.py # Unit tests for the BankAccount class. │ └── README.md 

# Project documentation.


---

## Prerequisites  
- Python 3.7 or later  
- `unittest` (bundled with Python’s standard library)  

---

## Setup Instructions  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/your-repo/bank-app.git
   cd bank-app
2. Navigate to the Project Directory:
   cd bank-app
   
3.Run Tests:
  Execute the test suite to ensure everything works as expected:
  python -m unittest discover -s tests

Running the Application
To use the BankAccount class:

Navigate to the src folder:

bash
Copy
Edit
cd src
Run the main.py file and interact with the BankAccount class as needed.

Example Usage
python
Copy
Edit
from main import BankAccount, NegativeAmountError, InsufficientFundsError

# Create a bank account
account = BankAccount("Alice", 500.0)

# Deposit funds
try:
    account.deposit(200.0)
    print(f"New Balance: {account.balance}")
except NegativeAmountError as e:
    print(e)

# Withdraw funds
try:
    account.withdraw(100.0)
    print(f"New Balance: {account.balance}")
except (NegativeAmountError, InsufficientFundsError) as e:
    print(e)

# Print account details
print(account)
Unit Testing
Unit tests are located in the tests folder. They cover:

Initial balance validation
Deposits and withdrawals
Negative amount handling
Insufficient funds errors
Account holder validation
To run the tests:

bash
Copy
Edit
python -m unittest discover -s tests
Logging
The application uses Python’s logging module to log deposit and withdrawal activities. Logs are printed to the console to track transactions during runtime.

Contribution
Contributions are welcome! Please fork the repository and submit a pull request.


