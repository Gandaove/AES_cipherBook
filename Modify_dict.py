# modify cipherBook
from os import system
from time import sleep
import Error_res
import File
import Input
import Menus


def expandLevel(content):
    name = Input.stdin('Please enter the item where you want to add: ')
    if Error_res.judgeInKeys(name, content.keys()):
        if Error_res.judgeDictType(content[name]):
            print('Not allowed to recover a dic!')
            return
    else:
        print('Warning: You are creating dic with 2 level!')
    item = Input.stdin('Please enter the new item: ')               # allow user to create empty item
    value = Input.stdin('Please enter the new value: ')
    if not Error_res.judgeNone(value):
        return
    obj = File.Value()
    obj.create(value)
    content.update({name: {item: obj}})
    print('Level added!')


def updateHint(item, content):
    if item not in content.keys():
        print("Adding...")
        return True
    if isinstance(content[item], dict) and content[item] != {}:
        print("Not allowed to update a dic!")
        return False
    print("Updating...")
    return True


def updateDic(content):
    item = Input.stdin("Please enter the item's name you want to update: ")        # allow user to create empty item
    if not updateHint(item, content):
        return
    value = Input.stdin('Please enter the new value: ')
    if not Error_res.judgeNone(value):
        return
    obj = File.Value()
    obj.create(value)
    content.update({item: obj})
    print('Book updated!')
    # else:
    #     print('Value is empty, not change!')


def changeKeyName(content):
    name = Input.stdin("Please enter the item's name you want to change: ")
    if not Error_res.judgeInKeys(name, content.keys()):
        print('Sorry, you have no such item!')
        return
    new_name = Input.stdin('Please enter the new name: ')
    if Error_res.judgeInKeys(new_name, content.keys()):
        print("Can't recover other obj; Not save change!")
        return
    content[new_name] = content.pop(name)
    print('Name changed!')


def deleteDic(content):
    print(content.keys())
    name = Input.stdin("Please enter the item's name you want to delete: ")
    if not Error_res.judgeInKeys(name, content.keys()):
        print('Sorry, you have no such item!')
        return
    content.pop(name)
    print('Item deleted!')


def findDic(content):
    name = Input.stdin("Please enter the item's name you want to find(empty: print all): ")
    if name == '':
        printDic(content, 0)
        system('pause')
        return

    def find(content, name, road):          # find item's name(key or value)
        if isinstance(content, dict):
            for key, value in content.items():
                state = 0
                if isinstance(value, File.Value):
                    if value.name == name:
                        print(road, end='')
                        print(key, ':', value.name)
                elif name == key:
                    if isinstance(value, dict):
                        print(road + key, end='')
                        printDic(content[name], 0)
                    else:
                        print(road, end='')
                        print(key, ':', value.name)
                else:                       # not found yet
                    road += key + ' --> '
                    if not isinstance(value, dict):
                        road = road.replace(key + ' --> ', '')
                    find(value, name, road)
                if not state:
                    road = road.replace(key + ' --> ', '')
    find(content, name, '')
    system('pause')


def printDic(dic, t):
    if isinstance(dic, dict):
        for key, value in dic.items():
            print('\n' + '\t' * t + key + ':', end='')
            if isinstance(value, dict):
                printDic(value, t + 1)
            else:
                print(' ' + value.name, end='')
    elif isinstance(dic, File.Value):
        print(dic.name)
    print()


def modify_dict(content, level=1):
    funs = {'1': updateDic, '2': changeKeyName,
            '3': deleteDic, '4': findDic, '6': expandLevel}
    while True:
        system('cls')
        print(content.keys())
        print('level:', level)
        choice = Menus.ModifyMenu()
        if choice in funs:
            funs[choice](content)
            sleep(1)
        elif choice == '5':
            name = Input.stdin('Level: ')
            if not Error_res.judgeInKeys(name, content.keys()):
                print('You have no such item!')
                sleep(1)
                continue
            if not Error_res.judgeDictType(content[name]):
                print('Latest level!')
                sleep(1)
                continue
            modify_dict(content[name], level + 1)
        elif choice == '7':
            break
        else:
            Error_res.wrongInput()


# def modify(cipherBook):
#     content = cipherBook.content
#     modify_dict(cipherBook.content, 1)
#     cipherBook.content = content
