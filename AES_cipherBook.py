# main
import Error_res
import Menus
import Function
from os import system


def main():
    funs = {'1': Function.firstTime, '2': Function.hadBook, '3': Function.MySQLOperate, '4': Function.Quit}
    while True:
        system('cls')
        choice = Menus.MainMenu()
        if choice in funs:
            funs[choice]()
        else:
            Error_res.wrongInput()


if __name__ == '__main__':
    main()
