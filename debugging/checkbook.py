class Checkbook:
    def __init__(self):
        # Initialize the checkbook with a balance of 0.0
        self.balance = 0.0

    def deposit(self, amount):
        # Deposit the given amount into the checkbook balance
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Withdraw the given amount from the checkbook if sufficient funds are available
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Display the current balance of the checkbook
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            # Handle deposit amount input with error handling
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the deposit amount.")
        elif action.lower() == 'withdraw':
            # Handle withdrawal amount input with error handling
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number for the withdrawal amount.")
        elif action.lower() == 'balance':
            # Display current balance
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
