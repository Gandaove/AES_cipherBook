# main
import Input
import Error_res
import Menus
import Function
from os import system


def main():
    while True:
        system('cls')
        choice = Menus.MainMenu()
        if choice == '1':
            Function.firstTime()
        elif choice == '2':
            Function.hadBook()
        elif choice == '3':
            decide = Input.stdin('Are you sure to exit? (y/n)')
            if decide == 'y':
                print('Goodbye!')
                Error_res.quitProgram()
            elif decide == 'n':
                continue
            else:
                Error_res.wrongInput()
        else:
            Error_res.wrongInput()


if __name__ == '__main__':
    main()
