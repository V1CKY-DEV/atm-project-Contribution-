import withdraw
import deposit
import show_history
import change_password
from info import info_display
from utils import clear_terminal
def clear_screen():
    clear_terminal()
    # function to clear the output of the screen

    print()  # print blank line after clearing the screen


def menu2(account):
    # account is a list of account info
    # account[0] id
    # account[1] name
    # account[2] password
    # account[3] balance

    print("\n---------Hello, {0}--------- ".format(account[1]))
    ch = int(input("\n1) show info \n2) show process history\n3) deposit\n4) withdraw\n"
                   "5) change password \n6) logout\n\nchoice>> "))

    clear_screen()
    if ch == 1:
        clear_screen()
        try:
            info_display(account)
        except KeyboardInterrupt:
            clear_screen()
            
        
    elif ch == 2:
        show_history.show_history(account)
    elif ch == 3:
        deposit.deposit(account)
    elif ch == 4:
        withdraw.withdraw(account)
    elif ch == 5:
        change_password.change_password(account)
    elif ch == 6:
        return
        # logout - go back to menu1
    else:
        print("ERROR: Wrong choice\n")

    menu2(account)
