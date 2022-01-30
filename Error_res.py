# deal with error and quit
from os import system
from sys import exit as Exit
from time import sleep


def wrongInput():
    print('Wrong input!!!!')
    sleep(1.5)


def wrongFile():
    print('Error in filename or path')
    sleep(1)


def quitProgram():
    system('pause')
    Exit()
