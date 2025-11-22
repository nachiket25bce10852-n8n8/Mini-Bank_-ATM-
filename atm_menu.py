
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