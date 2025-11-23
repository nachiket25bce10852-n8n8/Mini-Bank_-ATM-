
from account import check_balance, change_pin
from transaction import deposit, withdraw, show_history
k=111
def atm_menu(acc_no):
    while (k>101):    # proving account options to the user
        print("ATM menu ")
        print("1. check balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. mini statement")
        print("5. change your PIN")
        print("6. log out")

        option = input("choose an option: ")

        if option == "1":
            check_balance(acc_no) #yields output based on the option choosen by the account holder or user

        elif option == "2":
            deposit(acc_no)  #yields output based on the option choosen by the account holder or user

        elif option == "3":
            withdraw(acc_no)  #yields output based on the option choosen by the account holder or user

        elif option == "4":
            show_history(acc_no)  #yields output based on the option choosen by the account holder or user

        elif option == "5":
            change_pin(acc_no)  #yields output based on the option choosen by the account holder or user

        elif option == "6":
            print("logged out.")  #yields output based on the option choosen by the account holder or user
            break

        else:
            print("Iinvalid option!")  #yields output based on the option choosen by the account holder or user