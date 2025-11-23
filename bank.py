
from account import accounts

def create_account():
    print(" create new account ")
    acc_no = input("enter new account number: ") #generating new account credentials for the new user or holder

    if acc_no in accounts:
        print("account already exists!")  #analysed on the restored data
        return

    name = input("enter your name: ")
    pin = input("set a 4-digit PIN: ")

    accounts[acc_no] = {
        "name": name,
        "pin": pin,
        "balance": 0,
        "history": []
    }

    print("account created successfully!")   #new account added to the history


def login():
    print("login")
    acc_no = input("enter account number: ")
    pin = input("enter your PIN: ")

    if acc_no in accounts and accounts[acc_no]["pin"] == pin:
        print(f"welcome, {accounts[acc_no]['name']}")
        return acc_no
    else:
        print("invalid account number or PIN.")     #analysed on the restored data
        return None