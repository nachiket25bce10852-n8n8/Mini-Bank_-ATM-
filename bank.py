
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