
from account import accounts

def deposit(acc_no):
    amount = int(input("enter amount to deposit: "))
    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["history"].append(f"deposited ₹{amount}")
    print("deposit successful!")   # deposit money in the account

def withdraw(acc_no):     
    amount = int(input("enter amount to withdraw: "))  # withdraw money from the account
    if amount <= accounts[acc_no]["balance"]:
        accounts[acc_no]["balance"] -= amount
        accounts[acc_no]["history"].append(f"withdrew ₹{amount}")
        print("withdrawal successful!") # changes the current balance of the account
    else:
        print("insufficient balance!")  # when withdraw value is more than the current balance 
        

def show_history(acc_no):
    print("mini statement")
    if not accounts[acc_no]["history"]:
        print("no transactions yet.")
    else:
        for h in accounts[acc_no]["history"]:
            print(h)