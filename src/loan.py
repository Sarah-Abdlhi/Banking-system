class Loan:
    def __init__(self, loan_number, amount, customer_id, account_id, branch_id):
        """
        Initialize Loan object.

        Parameters:
        - loan_number (str): Loan number
        - amount (float): Loan amount
        - customer_id (str): ID of the customer applying for the loan
        - account_id (str): ID of the account related to the loan
        - branch_id (str): ID of the branch handling the loan
        """
        self.loan_number = loan_number
        self.amount = amount
        self.customer_id = customer_id
        self.account_id = account_id
        self.branch_id = branch_id

    def show_details(self):
        """
        Show details of the loan.
        """
        print(f"Loan Number: {self.loan_number}")
        print(f"Amount: {self.amount}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Account ID: {self.account_id}")
        print(f"Branch ID: {self.branch_id}")