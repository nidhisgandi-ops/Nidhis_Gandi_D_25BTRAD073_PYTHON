class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = float(initial_balance)
        self.__transactions = []

        if initial_balance > 0:
            self.__transactions.append(f"Initial Deposit: +₹{initial_balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print(
                f"[Error] Invalid deposit amount (₹{amount}). "
                "Amount must be greater than zero."
            )
            return False

        self.__balance += amount
        self.__transactions.append(f"Deposited: +₹{amount:.2f}")
        print(f"[Success] ₹{amount:.2f} deposited to {self.holder_name}'s account.")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print(
                f"[Error] Invalid withdrawal amount (₹{amount}). "
                "Amount must be greater than zero."
            )
            return False

        if amount > self.__balance:
            print(
                f"[Declined] Insufficient balance for ₹{amount:.2f} withdrawal. "
                f"Available: ₹{self.__balance:.2f}"
            )
            return False

        self.__balance -= amount
        self.__transactions.append(f"Withdrawn: -₹{amount:.2f}")
        print(f"[Success] ₹{amount:.2f} withdrawn from {self.holder_name}'s account.")
        return True

    def get_balance(self):
        print(
            f"Account: {self.account_number} | Holder: {self.holder_name} | "
            f"Current Balance: ₹{self.__balance:.2f}"
        )
        return self.__balance

    def print_statement(self):
        print(f"\n--- Mini Statement for {self.holder_name} ({self.account_number}) ---")
        for entry in self.__transactions:
            print(f" * {entry}")
        print(f"Final Balance: ₹{self.__balance:.2f}\n")


acc1 = BankAccount("ACC1001", "Vikram Desai", 5000.00)
acc1.get_balance()

print("\n--- Testing Valid Transactions ---")
acc1.deposit(2500.00)
acc1.withdraw(1200.00)
acc1.get_balance()

print("\n--- Testing Invalid Transactions & Edge Cases ---")
acc1.deposit(-500.00)
acc1.withdraw(0)
acc1.withdraw(10000.00)

print("\n--- Testing Encapsulation ---")
try:
    print(acc1.__balance)
except AttributeError:
    print("Security Check Passed: Direct access to '__balance' is blocked!")

acc1.print_statement()
