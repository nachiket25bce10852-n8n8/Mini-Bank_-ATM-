
# This dictionary stores all accounts in memory
accounts = {}

def check_balance(acc_no):
    print(f"Your balance is: ₹{accounts[acc_no]['balance']}")

def change_pin(acc_no):
    new_pin = input("Enter new 4-digit PIN: ")
    accounts[acc_no]["pin"] = new_pin
    print("PIN changed successfully!")