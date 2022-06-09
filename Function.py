# lead functions
import Menus
import Error_res
import Modify_dict
import Security
import book
import sql
import Input
from time import sleep
from os import system


def firstTime():
    print("Warning: You must Set your Key(Can't be 'None')")
    cipherBook = book.BookCreate()
    cipherBook.run()
    sleep(2.5)
    return optionsFuction(cipherBook)


def hadBook():
    cipherBook = book.BookFromFile()
    cipherBook.run()
    cipherBook.verify()
    sleep(1)
    return optionsFuction(cipherBook)


# @Error_res.while_execute
def optionsFuction(cipherBook):
    while True:
        system('cls')
        choice = Menus.BookMenu()
        if choice == '1':
            # Modify_dict.modify(cipherBook)
            Modify_dict.modify(cipherBook)
        elif choice == '2':
            Security.security(cipherBook)
        elif choice == '3':           # choose save or not
            cipherBook.saveChange()
            break
        else:
            Error_res.wrongInput()


def MySQLOperate():
    while True:
        system('cls')
        choice = Menus.MySQLMenu()
        if choice == '1':
            sql.saveToSQL()
        elif choice == '2':
            sql.deleteFromSQL()
        elif choice == '3':
            sql.saveToFile()
        elif choice == '4':
            break
        else:
            Error_res.wrongInput()


def Quit():
    decide = Input.stdin('Are you sure to exit? (y/n)')
    if decide == 'y' or decide == '':
        print('Goodbye!')
        Error_res.quitProgram()
    elif decide == 'n':
        pass
    else:
        Error_res.wrongInput()
