from src.customer import Customer  # Import Customer class from customer.py
from src.admin import Admin  # Import Admin class from admin.py
from src.bank import Bank  # Import Bank class from bank.py
from src.branch import Branch  # Import Branch class from branch.py
from src.account import Account  # Import Account class from account.py
from src.exception import InsufficientBudgetError  # Import custom exception class

def main():
    while True:
        print("Welcome to the Bank System!")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")

        choice = input("Please select your role: ")

        if choice == "1":
            admin_menu()  # Call admin_menu function if choice is 1
        elif choice == "2":
            customer_menu()  # Call customer_menu function if choice is 2
        elif choice == "3":
            break  # Break the loop if choice is 3
        else:
            print("Invalid choice. Please try again.")  # Print error message for invalid choice

def admin_menu():
    admin_name = input("Enter Admin name: ")
    admin_family = input("Enter Admin family: ")
    admin_national_id = input("Enter Admin national ID: ")
    admin_password = input("Enter Admin password: ")

    if Admin.check_password(admin_password):
        #after checking the password an instance of admin is created
        admin = Admin(admin_name, admin_family, admin_national_id, admin_password)  # Create Admin object



    while True:
        print("\nAdmin Menu:")
        print("1. Create Bank")
        print("2. Create Branch")
        print("3. Delete Bank")
        print("4. Delete Branch")
        print("5. Change Password")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter bank name: ")
            bank_id = input("Enter bank ID: ")
            admin.create_bank(name, bank_id)  # Call create_bank method of Admin class
        elif choice == "2":
            name = input("Enter branch name: ")
            branch_id = input("Enter branch ID: ")
            budget = int(input("Enter branch budget: "))
            city_name = input("Enter city name: ")
            admin.create_branch(name, branch_id, budget, city_name)  # Call create_branch method of Admin class
        elif choice == "3":
            bank_id = input ("Enter the bank_id:")
            for bank in Bank.Bank_list:
                if bank.bank_id == bank_id:
                    Bank.Bank_list.remove(bank)
            # Implement Delete Bank
        elif choice == "4":
            # Implement Delete Branch
            branch_id = input ("Enter the branch_id:")
            for branch in Branch.Branch_list:
                if branch.branch_id == branch_id:
                    Branch.Branch_list.remove(branch)
        elif choice == "5":
            current_pass = input("Enter current password: ")
            new_pass = input("Enter new password: ")
            if admin.change_password(current_pass, new_pass):
                print("Password changed successfully.")
            else:
                print("Password change failed. Invalid current password.")
        elif choice == "6":
            exit()
        else:
            print("Invalid choice. Please try again.")  # Print error message for invalid choice

def customer_menu():
    name = input("Enter your name: ")
    family = input("Enter your family: ")
    national_id = input("Enter your national ID: ")
    home_town = input("Enter your home town: ")

    customer = Customer(name, family, national_id, home_town)  # Create Customer object

    while True:
        print("\nCustomer Menu:")
        print("1. Show Details")
        print("2. Loan Request")
        print("3. Deposit")
        print("4. Withdrawal")
        print("5. Open Account")
        print("6. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer.show_details(national_id)  # Call show_details method of Customer class
        elif choice == "2":
            account_number = input("Enter account number: ")
            loan_amount = int(input("Enter loan amount: "))
            branch_id = input("Enter branch id: ")
            branch_budget = 0 # defined as a global variable
            for branch in Branch.Branch_list:
                if branch.branch_id == branch_id:
                    branch_budget = branch.budget # get budget from Branch based on the branch_id entered by the user
            try:
                if customer.loan_request(national_id, account_number, loan_amount, branch_budget, branch_id):
                    print("Loan request accepted.")
                else:
                    print("Loan request denied.")
            except:
                insufficientBudgetError = InsufficientBudgetError()
                # an instance created from the class
                insufficientBudgetError.insufficient_budget()
                
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = int(input("Enter amount to deposit: "))
            if customer.deposit(account_number, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed. Invalid account number.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = int(input("Enter amount to withdraw: "))
            if customer.withdrawal(account_number, amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed. Invalid account number.")
        elif choice == "5":
            account_number = customer.open_account()  # Call open_account method of Customer class
            print(f"Account opened successfully. Account number: {account_number}")
 
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")  # Print error message for invalid choice

if __name__ == "__main__":
    main()  # Call main function if the script is run directly
