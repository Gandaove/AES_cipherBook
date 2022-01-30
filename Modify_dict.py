# modify cipherBook
import Menus
import Input
from os import system
from time import sleep


def expandLevel(content):
    name = Input.stdin('Please enter the item where you want to add: ')
    if name in content.keys():
        if isinstance(content[name], dict):
            print('Not allowed to recover a dic!')
            return
    else:
        print('Warning: You are creating dic with 2 level!')
    item = Input.stdin('Please enter the new item: ')
    if item:
        value = Input.stdin('Please enter the new value: ')
        if value:
            content.update({name: {item: value}})
            print('Level added!')
        else:
            print('One of variables empty, not save change!')
    else:
        print('Item is empty, not save change!')


def updateDic(content):
    item = Input.stdin('Please enter the name of the item you want to update: ')
    if item:
        if item in content.keys():                          # item exist
            if isinstance(content[item], dict):         # item is not a dict
                print('Not allowed to update a dic!')
                return
            else:
                print('Updating.....')
        else:                                               # item not exist
            print('Adding.....')
    else:
        print('Item is empty, not save change!')
        return

    value = Input.stdin('Please enter the new value: ')
    if value:
        content.update({item: value})
        print('Book updated!')
    else:
        print('Value is empty, not change!')


def deleteDic(content):
    print(content.keys())
    name = Input.stdin('Please enter the name of the item you want to delete: ')
    if name in content.keys():
        content.pop(name)
        print('Item deleted!')
    else:
        print('Sorry, you have no such item!')


def findDic(content, name):
    if name:
        if isinstance(content, dict):
            for key, value in content.items():
                if name == key or name == value:
                    print(key + ': ' + value)
                else:
                    findDic(value, name)
    else:
        printDic(content, 0)
        print()


def printDic(dic, t):
    if isinstance(dic, dict):
        for key, value in dic.items():
            print('\n' + '\t' * t + key + ':', end='')
            if isinstance(value, dict):
                printDic(value, t + 1)
            else:
                print(' ' + value, end='')
    else:
        print(dic)


def modify_dict(content, name, level):
    while True:
        system('cls')
        print(content.keys())
        print('level:', level)
        choice = Menus.ModifyMenu()
        if choice == '1':
            updateDic(content)
            sleep(1)
        elif choice == '2':
            deleteDic(content)
            sleep(1)
        elif choice == '3':
            item = Input.stdin(
                'Please enter the name of the item you want to find(empty: print all): ')
            findDic(content, item)
            system('pause')
        elif choice == '4':
            name = Input.stdin('Level: ')
            if name in content.keys():
                if isinstance(content[name], dict):
                    modify_dict(content[name], name, level + 1)
                else:
                    print('Latest level!')
                    sleep(1)
            else:
                print('You have no such item!')
                sleep(1)
        elif choice == '5':
            expandLevel(content)
            sleep(1)
        elif choice == '6':
            break
        else:
            print('Wrong input!')
            sleep(1.5)
