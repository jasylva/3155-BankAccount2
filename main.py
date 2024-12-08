from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount

# Create instances of CheckingAccount and SavingsAccount
checking_account = CheckingAccount("Eve", 2000, 100,
                                   "999999999", "111111111", 500)
savings_account = SavingsAccount("Eve", 3000, 200,
                                 "888888888", "222222222", 2.0)

# Scenario: Withdraw from Checking Account and deposit to Savings Account
print("Initial Balance for Checking Account: " + str(checking_account.customer_balance))
print("Withdraw $500 from Checking Account: ")
checking_account.withdraw(500)
print("Balance after withdrawal for Checking Account: " + str(checking_account.customer_balance))
print("\n")

print("Initial Balance for Savings Account: " + str(savings_account.customer_balance))
print("Deposit into Savings Account: ")
savings_account.deposit(500)
print("Balance after deposit into Savings Account: " + str(savings_account.customer_balance))

