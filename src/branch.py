class Branch:
    Branch_list = []
   
    def __init__(self, name, branch_id, budget, city_name, num_customers=0):
        """
        Initialize Branch object.

        Parameters:
        - name (str): Name of the branch
        - branch_id (str): ID of the branch
        - num_customers (int): Number of customers
        - budget (int): Budget of the branch
        - city_name (str): Name of the city
        """
        self.name = name
        self.branch_id = branch_id
        self.num_customers = num_customers
        self.budget = budget
        self.city_name = city_name
        Branch.Branch_list.append(self)
        #Each time a branch is added it will be appended to the list

    def show_details(self):
        """
        Show details of the branch.
        """
        print(f"Branch Name: {self.name}, Branch ID: {self.branch_id}, Number of Customers: {self.num_customers}, Budget: {self.budget}, City Name: {self.city_name}")
