from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, customer_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount):
        if amount <= self.transfer_limit:
            self.customer_balance -= amount
            return self.customer_balance
        else:
            return "Transfer limit exceeded"