# create Accounts.txt if not exist
# Changed the name of atm.py to main.py which is how everyone uses the starting file of python, like i dont know which file is the starting file so its hard to check and read the code so make sure to always use the starting file or main file as main.py
try:
    # read the 'Accounts.txt' file
    # if you try to open non existing file in read mode, this will throw an error
    f = open('Accounts.txt', 'r')
    f.close()
except FileNotFoundError:
    # if 'Accounts.txt' file is not found, create it
    f = open('Accounts.txt', 'w')
    f.close()

# import modules
import menu1
import os
from utils import clear_terminal
clear_terminal()
menu1.menu1()  # start the program - call menu1() function
