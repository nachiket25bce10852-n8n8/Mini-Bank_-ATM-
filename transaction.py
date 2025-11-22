
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