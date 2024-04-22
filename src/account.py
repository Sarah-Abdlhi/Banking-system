import random

class Account:
    def __init__(self, account_number, owner, balance=0):
        """
        Initialize Account object.

        Parameters:
        - account_number (str): Account number
        - owner (str): Name of the account owner
        - balance (float): Initial balance of the account (default: 0)
        """
        self.account_number = account_number
        self.owner = owner
        self.balance = balance


    def generate_account_number():
        """
        Generate a random and unique 8-digit account number.

        Returns:
        - str: Generated account number
        """
        return ''.join(str(random.randint(0, 9)) for _ in range(8))


    def show_details(self):
        """
        Show details of the account.
        """
        print(f"Account Number: {self.account_number}, Balance: {self.balance}, Owner: {self.owner}")
