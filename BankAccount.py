class BankAccount:
    # Class attribute Title of bank
    title = "Bank Title"

    # Instance variables
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.customer_balance = customer_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member

    # Methods
    def deposit(self, amount):
        self.customer_balance += amount
        return self.customer_balance

    def withdraw(self, amount):
        if self.customer_balance - amount >= self.minimum_balance:
            self.customer_balance -= amount
        else:
            return "Insufficient balance"
        return self.customer_balance

    def print_customer_information(self):
        print(f"{self.title}: Customer Name: {self.customer_name}, "
              f"Customer Balance: {self.customer_balance}, Minimum Balance: {self.minimum_balance}, "
              f"Account Number: {self._account_number}")

    def get_routing_number(self):
        return self.__routing_number
