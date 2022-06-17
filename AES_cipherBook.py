# main
import Error_Res
import Menus
import Function


def main():
    funs = {'1': Function.firstTime, '2': Function.hadBook, '3': Function.MySQLOperate, '4': Function.Quit}
    while True:
        Error_Res.clearScreen()
        choice = Menus.MainMenu()
        if choice not in funs:
            Error_Res.wrongInput()
            continue
        funs[choice]()
            


if __name__ == '__main__':
    main()
