# PREPARING MINI-BANK_ATM #


from account import accounts

def deposit(acc_no):
    amount = int(input("Enter amount to deposit: "))
    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["history"].append(f"Deposited ₹{amount}")
    print("Deposit successful!")

def withdraw(acc_no):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= accounts[acc_no]["balance"]:
        accounts[acc_no]["balance"] -= amount
        accounts[acc_no]["history"].append(f"Withdrew ₹{amount}")
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")

def show_history(acc_no):
    print("\n--- Mini Statement ---")
    if not accounts[acc_no]["history"]:
        print("No transactions yet.")
    else:
        for h in accounts[acc_no]["history"]:
            print(h)

# This dictionary stores all accounts in memory
accounts = {}

def check_balance(acc_no):
    print(f"Your balance is: ₹{accounts[acc_no]['balance']}")

def change_pin(acc_no):
    new_pin = input("Enter new 4-digit PIN: ")
    accounts[acc_no]["pin"] = new_pin
    print("PIN changed successfully!")


from account import check_balance, change_pin
from transaction import deposit, withdraw, show_history

def atm_menu(acc_no):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Logout")

        option = input("Choose an option: ")

        if option == "1":
            check_balance(acc_no)

        elif option == "2":
            deposit(acc_no)

        elif option == "3":
            withdraw(acc_no)

        elif option == "4":
            show_history(acc_no)

        elif option == "5":
            change_pin(acc_no)

        elif option == "6":
            print("Logged out.")
            break

        else:
            print("Invalid option!")


from account import accounts

def create_account():
    print("\n--- Create New Account ---")
    acc_no = input("Enter new account number: ")

    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter your name: ")
    pin = input("Set a 4-digit PIN: ")

    accounts[acc_no] = {
        "name": name,
        "pin": pin,
        "balance": 0,
        "history": []
    }

    print("Account created successfully!")


def login():
    print("\n--- Login ---")
    acc_no = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(f"Welcome, {accounts[acc_no]['name']}!")
        return acc_no
    else:
        print("Invalid account number or PIN.")
        return None

from bank import create_account, login
from atm_menu import atm_menu

def main():
    while True:
        print("\n=========== MINI BANK ATM ===========")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            acc_no = login()
            if acc_no:
                atm_menu(acc_no)

        elif choice == "3":
            print("Thank you for using Mini Bank ATM!")
            break

        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()