from src.person import Person
from src.bank import Bank
from src.branch import Branch

class Admin(Person):
    def __init__(self, name, family, national_id, password):
        """
        Initialize Admin object.

        Parameters:
        - name (str): Name of the admin
        - family (str): Family name of the admin
        - national_id (str): National ID of the admin
        - password (str): Password of the admin
        """
        self.name = name
        self.family = family
        self.national_id = national_id
        self.password = password

    @classmethod
    # can access the method withought creating instance/ it is assigned as a feature
    def check_password(self, password):
        """
        Check if the given password matches the admin's password.

        Parameters:
        - password (str): Password to check

        Returns:
        - bool: True if the passwords match, False otherwise
        """
        with open("admin-password.txt", "r") as file:
            admin_password = file.readline().strip()
            return password == admin_password

    def show_data(self, **kwargs):
        """
        Show data.

        Parameters:
        - **kwargs: Keyword arguments for data to show
        """
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    def create_bank(self, name, bank_id):
        """
        Create a new bank.

        Parameters:
        - name (str): Name of the bank
        - bank_id (str): ID of the bank
        """
        bank = Bank(name, bank_id)
        #instance created

    def create_branch(self, name, branch_id, budget, city_name, num_customers=0):
        """
        Create a new branch.

        Parameters:
        - name (str): Name of the branch
        - branch_id (str): ID of the branch
        - num_customers (int): Number of customers
        - budget (int): Budget of the branch
        - city_name (str): Name of the city
        """
        branch = Branch(self, name, branch_id, budget, city_name, num_customers)

    def change_password(self, current_pass, new_pass):
        """
        Change admin's password.

        Parameters:
        - current_pass (str): Current password
        - new_pass (str): New password

        Returns:
        - bool: True if the password is changed successfully, False otherwise
        """
        if self.check_password(current_pass):
            self.password = new_pass
            with open("admin-password.txt", "w") as file:
                file.write(new_pass)
            return True
        else:
            return False

    @classmethod
    def check_budget_for_loan(self, branch_id, loan_amount):
        """
        Check if there is budget to give loan.

        Parameters:
        - branch_id (str): ID of the branch
        - loan_amount (float): Amount of the loan

        Returns:
        - bool: True if there is sufficient budget, False otherwise
        """
        # implement this method according to your requirements
        for branch in Branch.Branch_list:
            if branch.branch_id == branch_id:
                if branch.budget >= loan_amount:
                    return True
                