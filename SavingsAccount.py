from BankAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number, interest):
        super().__init__(customer_name, customer_balance, minimum_balance, account_number, routing_number)
        self.interest = interest

    def add_interest(self):
        self.customer_balance += self.customer_balance * self.interest
        return self.customer_balance
