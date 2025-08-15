# Bank Management System in Python
# Author: Jahanavi

import os
import pickle

# Bank Account Class
class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\n₹{amount} deposited successfully. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("\nInsufficient balance!")
        else:
            self.balance -= amount
            print(f"\n₹{amount} withdrawn successfully. New Balance: ₹{self.balance}")

    def display_account(self):
        print(f"Account No: {self.acc_no}")
        print(f"Name      : {self.name}")
        print(f"Type      : {self.acc_type}")
        print(f"Balance   : ₹{self.balance}")

# Save data to file
def save_accounts(accounts):
    with open("bank_data.dat", "wb") as f:
        pickle.dump(accounts, f)

# Load data from file
def load_accounts():
    if os.path.exists("bank_data.dat"):
        with open("bank_data.dat", "rb") as f:
            return pickle.load(f)
    return {}

# Create new account
def create_account(accounts):
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("\nAccount already exists!")
        return
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (Savings/Current): ")
    balance = float(input("Enter Initial Deposit: ₹"))
    accounts[acc_no] = BankAccount(acc_no, name, acc_type, balance)
    save_accounts(accounts)
    print("\nAccount created successfully!")

# Deposit money
def deposit_money(accounts):
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to deposit: ₹"))
        accounts[acc_no].deposit(amount)
        save_accounts(accounts)
    else:
        print("\nAccount not found!")

# Withdraw money
def withdraw_money(accounts):
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter amount to withdraw: ₹"))
        accounts[acc_no].withdraw(amount)
        save_accounts(accounts)
    else:
        print("\nAccount not found!")

# Display account details
def display_account(accounts):
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        accounts[acc_no].display_account()
    else:
        print("\nAccount not found!")

# Main Menu
def main():
    accounts = load_accounts()

    while True:
        print("\n===== Bank Management System =====")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Details")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            display_account(accounts)
        elif choice == "5":
            print("\nThank you for using Bank Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()
