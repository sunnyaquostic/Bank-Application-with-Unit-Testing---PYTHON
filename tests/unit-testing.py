import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.main import BankAccount, NegativeAmountError, InsufficientFundsError

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        print("Setting up the test...")
        self.wallet = BankAccount("Bush", 1000.0)
    
    # test initial deposit 
    def test_initial_balance(self):
        self.assertEqual(self.wallet.balance, 1000.0)
        self.assertTrue(self.wallet.balance >= 0)
        
    # test deposit
    def test_deposit(self):
        self.wallet.deposit(500.0)
        self.assertEqual(self.wallet.balance, 1500.0)
        self.assertGreater(self.wallet.balance, 1000.0)
        
    # test withdraw
    def test_withdraw(self):
        old_balance = self.wallet.balance
        self.wallet.withdraw(100.0)
        self.assertEqual(self.wallet.balance, 900.0)
        self.assertNotEqual(self.wallet.balance, old_balance)
    
    # test negative deposit
    def test_negative_deposit(self):
        with self.assertRaises(NegativeAmountError):
            self.wallet.deposit(-10000.0)
       
    #   test insufficient funds
    def test_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.wallet.withdraw(10000.0)
            
    # test negative withdraw
    def test_negative_deposit(self):
        with self.assertRaises(NegativeAmountError):
            self.wallet.withdraw(-100.0)
            
    # test account holder
    def test_account_holder(self):
        self.assertIsNotNone(self.wallet.account_holder)
        self.assertEqual(self.wallet.account_holder, "Bush")
       
        
    def tearDown(self):
        self.wallet = None
        
if __name__ == "__main__":
    unittest.main()