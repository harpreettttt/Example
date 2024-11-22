# test_bank_account.py

import unittest
# from bank_account import BankAccount


class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float, account_type: str): #parameter you are just passing these so it knows what the class is made of. dont need to encapsulate here.
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.__account_type = account_type

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """
        Set up a BankAccount object for testing.
        This method is called before each test.
        """
        self.account = BankAccount(
            account_number="1234567890",
            account_holder="John Doe",
            balance=1000.00,
            account_type="Savings"
        )

    def test_initialization(self):
        """
        Test that the BankAccount object is initialized correctly.
        """
        self.assertEqual(self.account.get_account_number(), "1234567890")
        self.assertEqual(self.account.get_account_holder(), "John Doe")
        self.assertEqual(self.account.get_account_type(), "Savings")
        self.assertEqual(self.account.get_balance(), 1000.00)

    def test_deposit_positive_amount(self):
        """
        Test depositing a positive amount increases the balance correctly.
        """
        self.account.deposit(500.00)
        self.assertEqual(self.account.get_balance(), 1500.00)

    def test_deposit_zero_amount(self):
        """
        Test that depositing zero raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.account.deposit(0)
        self.assertEqual(str(context.exception), "Deposit amount must be positive.")

    def test_deposit_negative_amount(self):
        """
        Test that depositing a negative amount raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100)
        self.assertEqual(str(context.exception), "Deposit amount must be positive.")

    def test_withdraw_positive_amount(self):
        """
        Test withdrawing a positive amount decreases the balance correctly.
        """
        self.account.withdraw(300.00)
        self.assertEqual(self.account.get_balance(), 700.00)

    def test_withdraw_zero_amount(self):
        """
        Test that withdrawing zero raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(0)
        self.assertEqual(str(context.exception), "Withdrawal amount must be positive.")

    def test_withdraw_negative_amount(self):
        """
        Test that withdrawing a negative amount raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-50)
        self.assertEqual(str(context.exception), "Withdrawal amount must be positive.")

    def test_withdraw_insufficient_funds(self):
        """
        Test that withdrawing more than the balance raises a ValueError.
        """
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(1500.00)
        self.assertEqual(str(context.exception), "Insufficient funds.")

    def test_get_balance(self):
        """
        Test that get_balance returns the correct balance.
        """
        self.assertEqual(self.account.get_balance(), 1000.00)
        self.account.deposit(200.00)
        self.assertEqual(self.account.get_balance(), 1200.00)
        self.account.withdraw(300.00)
        self.assertEqual(self.account.get_balance(), 900.00)

    def test_get_account_details(self):
        """
        Test that get_account_details returns the correct formatted string.
        """
        expected_details = ("Account Number: 1234567890, Account Holder: John Doe, "
                            "Account Type: Savings, Balance: 1000.00")
        self.assertEqual(self.account.get_account_details(), expected_details)

    def test_multiple_transactions(self):
        """
        Test a sequence of deposits and withdrawals.
        """
        self.account.deposit(500.00)   # Balance: 1500.00
        self.account.withdraw(200.00)  # Balance: 1300.00
        self.account.deposit(300.00)   # Balance: 1600.00
        self.account.withdraw(1600.00) # Balance: 0.00
        self.assertEqual(self.account.get_balance(), 0.00)

    def test_account_type(self):
        """
        Test that the account type is set correctly.
        """
        self.assertEqual(self.account.get_account_type(), "Savings")
        # Optionally, test with a different account type
        checking_account = BankAccount(
            account_number="0987654321",
            account_holder="Jane Smith",
            balance=500.00,
            account_type="Checking"
        )
        self.assertEqual(checking_account.get_account_type(), "Checking")

    def test_account_holder_name(self):
        """
        Test that the account holder's name is set correctly.
        """
        self.assertEqual(self.account.get_account_holder(), "John Doe")
        # Optionally, test with a different account holder
        another_account = BankAccount(
            account_number="1122334455",
            account_holder="Alice Johnson",
            balance=750.00,
            account_type="Savings"
        )
        self.assertEqual(another_account.get_account_holder(), "Alice Johnson")

if __name__ == '__main__':
    unittest.main()
