
from bank import create_account, login
from atm_menu import atm_menu
A=101
def master():
    while (A>100):
        print(" My mini bank ATM ")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit") # gives choices to the user 

        choice = input("choose an option: ")

        if choice == "1":
            create_account() # creates an new account

        elif choice == "2":
            acc_no = login()
            if acc_no:
                atm_menu(acc_no) 

        elif choice == "3":
            print("thank you for using Mini Bank ATM!")
            break
        
# the option you wil choose will lead you to the next steps
        else:
            print("invalid choice, try again!")

if __name__ == "__master__":
    master()