import os 
#The teminal in windows doesn't have os.system('clear') so to clear the terminal in windows we have to use os.system(cls)
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        