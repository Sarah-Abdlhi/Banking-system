from src.person import Person
from src.branch import Branch
import random
from src.admin import Admin
from src.account import Account

class Customer(Person):
    def __init__(self, name, family, national_id, home_town):
        """
        Initialize Customer object.

        Parameters:
        - name (str): Name of the customer
        - family (str): Family name of the customer
        - national_id (str): National ID of the customer
        - home_town (str): Home town of the customer
        """
        self.name = name
        self.family = family
        self.national_id = national_id
        self.home_town = home_town
        self.account_numbers = []  # List of account numbers
     

    def show_details(self):
        """
        Show details of the customer.
        """
        print(f"Name: {self.name}")
        print(f"Family: {self.family}")
        print(f"National ID: {self.national_id}")
        print(f"Home Town: {self.home_town}")
        print(f"Account Numbers: {self.account_numbers}")
  

    def loan_request(self, account_number, loan_amount,branch_id):
        """
        Request a loan.

        Parameters:
        - account_number (str): Account number
        - loan_amount (float): Amount of the loan
        -  branch_id

        Returns:
        - bool: True if the loan request is successful, False otherwise
        """
        # Check if the branch has sufficient budget for the loan
        if Admin.check_budget_for_loan(branch_id, loan_amount):
            # Update loan information
            
            loan_number = self.generate_loan_number()
            #generated loan number is added as the value of loan_number variable
            self.loan_number.append(loan_number)
            # new loan nnumber added to the previous existing ones

            return True
        else:
            return False

    def deposit(self, amount, account_number):
        """
        Deposit money into the account.

        Parameters:
        - amount (float): Amount to deposit
        """
        for acc_no in Account.account_number:
            if acc_no.account_number == account_number:
                acc_no.balance += amount

    def withdrawal(self, account_number, amount):
        """
        Withdraw money from the account.

        Parameters:
        - amount (float): Amount to withdraw
        """
        for acc_no in Account.account_number:
            if acc_no.account_number == account_number:       
                if acc_no.balance >= amount:
                    acc_no.balance -= amount
        else:
            print("Insufficient funds")

    def open_account(self):
        """
        Open a new account for the customer.
        """
        account = Account(None, owner=self.national_id, balance = 0)
        #initial account_number = none
        account_number = account.generate_account_number()
        account.account_number = account_number
        #update none with the gnerated acc no 
        self.account_numbers.append(account_number)
        branch_id = 0
        # globally defined
        for customer in Customer.customer_list:
            if customer.account_number == account_number:
                branch_id = customer.branch_id
        for branch in Branch. branch_list:
            if branch.branch_id == branch_id:
                branch.num_customers += 1
        #each time an account is created the number of customers is updated

    def generate_loan_number(self):
        """
        Generate a unique loan number.

        Returns:
        - str: Generated loan number
        """
        return ''.join(str(random.randint(0, 9)) for _ in range(6))