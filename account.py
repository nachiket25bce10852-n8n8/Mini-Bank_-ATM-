
# This dictionary stores all accounts in memory
accounts = {}

def check_balance(acc_no):
    print(f"so, your current account balance is ₹{accounts[acc_no]['balance']}.")

def change_pin(acc_no):
    new_pin = input("enter new 4-digit PIN: ")  #setting up new pin
    accounts[acc_no]["pin"] = new_pin
    print("pin changed successfully!") # finally pin changed successfully