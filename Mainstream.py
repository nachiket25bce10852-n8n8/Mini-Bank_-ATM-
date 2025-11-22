
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