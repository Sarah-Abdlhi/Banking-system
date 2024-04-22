class Bank:
    Bank_list = []
    def __init__(self, name, bank_id):
        """
        Initialize Bank object.

        Parameters:
        - name (str): Name of the bank
        - bank_id (str): ID of the bank
        """
        self.name = name
        self.bank_id = bank_id
        Bank.Bank_list.append(self)


    def show_details(self):
        """
        Show details of the bank.
        """
        print(f"Bank Name: {self.name}, BAnk ID:{self.bank_id}")
