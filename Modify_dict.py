# modify cipherBook
from time import sleep
from pathlib import Path
import Error_Res
import File
import Input
import Menus


def expandLevel(content):
    name = Input.stdin('Please enter the item where you want to add: ')
    if Error_Res.judgeInKeys(name, content.keys()):
        if Error_Res.judgeDictType(content[name]):
            print('Not allowed to recover a dic!')
            return
    else:
        print('Warning: You are creating dic with 2 level!')
    item = Input.stdin('Please enter the new item: ')
    if not Error_Res.judgeNotNone(item):
        return
    value = Input.stdin('Please enter the new value: ')
    obj = File.Value()
    obj.create(value)
    content.update({name: {item: obj}})
    print('Level added!')


def updateHint(item, content):
    if not Error_Res.judgeNotNone(item):
        return False
    if Error_Res.judgeInKeys(item, content.keys()):
        if Error_Res.judgeDictType(content[item]):
            print("Not allowed to update a dic!")
            return False
        print("Updating...")
        return True
    print("Adding...")
    return True


def updateDic(content):
    item = Input.stdin("Please enter the item's name you want to update: ")        # allow user to create empty item
    if not updateHint(item, content):
        return
    value = Input.stdin('Please enter the new value: ')
    obj = File.Value()
    obj.create(value)
    content.update({item: obj})
    print('Book updated!')
    # else:
    #     print('Value is empty, not change!')


def changeKeyName(content):
    name = Input.stdin("Please enter the item's name you want to change: ")
    if not Error_Res.judgeInKeys(name, content.keys()):
        print('Sorry, you have no such item!')
        return
    new_name = Input.stdin('Please enter the new name: ')
    if Error_Res.judgeInKeys(new_name, content.keys()):
        print("Can't recover other obj; Not save change!")
        return
    content[new_name] = content.pop(name)
    print('Name changed!')


def deleteDic(content):
    print(content.keys())
    name = Input.stdin("Please enter the item's name you want to delete: ")
    if not Error_Res.judgeInKeys(name, content.keys()):
        print('Sorry, you have no such item!')
        return
    content.pop(name)
    print('Item deleted!')


def findDic(content):
    name = Input.stdin("Please enter the item's name you want to find(empty: print all): ")
    if not Error_Res.judgeNotNone(name):
        print(printDic(content))
        Error_Res.pauseProgram()
        return

    def find(content, name, road=''):          # find item's name(key or value)
        if Error_Res.judgeDictType(content):
            for key, value in content.items():
                # state = 0
                if Error_Res.judgeValueType(value):
                    if value.name == name:
                        road += key + ':' + value.name
                elif name == key:
                    if Error_Res.judgeDictType(value):
                        road += key
                        road += printDic(content[name], string=road)
                    else:
                        road += key + ':' + value.name
                else:                       # not found yet
                    road += key + ' --> '
                    if not Error_Res.judgeValueType(value):
                        road = road.replace(key + ' --> ', '')
                    road = find(value, name, road)
                # if not state:
                #     road = road.replace(key + ' --> ', '')
        return road
    
    def findOptimize(content, name, road=''):
        for key, value in content.items():
            if name == key:
                if Error_Res.judgeDictType(value):          # name equal key, and value is a dict (maybe empty)
                    road += name + '(value is dict)(equal to key) ' + '\n'
                    road += printDic(dic=content[name], string=road)
                    break
                else:                                       # name equal key, and value is Value
                    road += name + '(value is Value)(equal to key) ' + value.__repr__() + '\n'
                    break
            elif name == value.__repr__():                  # name equal value.name
                road += key + '(equal to value.name) ' + name + '\n'
                break
            else:                                           # name not equal key or value.name
                # if Error_Res.judgeValueType(value):
                #     road = road.replace(key + ' --> ', '', 1)
                if Error_Res.judgeDictType(value):
                    road += key + ' --> '
                    road = findOptimize(value, name, road)
        return road
    # print(find(content, name))
    print(findOptimize(content, name))
    Error_Res.pauseProgram()
    return


def printDic(dic, t=0, string=''):
    if Error_Res.judgeDictType(dic):
        for key, value in dic.items():
            string += '\n' + '\t' * t + key + '>>'
            if value == {}:
                continue
            if Error_Res.judgeDictType(value):              # value is a dict
                string = printDic(value, t+1, string)
            else:                                           # value is a value
                # print(' ' + value.name, end='')
                string += ' ' + value.__repr__()
    elif Error_Res.judgeValueType(dic):
        string += dic.__repr__()
    # string += '\n'
    return string


def saveAsPlain(content, bookname):
    plain_dir = Path(bookname)
    plain_dir.mkdir(parents=True, exist_ok=True)     # create dir if not exist
    def traverse(content):
        for key, value in content.items():
            if Error_Res.judgeValueType(value):
                if value.valuetype == 'bytes':
                    value.writeFile(path=plain_dir/value.name, content=value.thing)
            elif Error_Res.judgeDictType(value):
                traverse(content[key])
    File.File.writeFile(path=plain_dir/(bookname+'.txt'), content=printDic(content).encode())
    traverse(content)
    print("Save Complete!")


def modify_dict(content, bookname, level=1):
    funs = {'1': updateDic, '2': changeKeyName,
            '3': deleteDic, '4': findDic, '6': expandLevel}
    while True:
        Error_Res.clearScreen()
        print(content.keys())
        print('level:', level)
        choice = Menus.ModifyMenu()
        if choice in funs:
            funs[choice](content)
            sleep(1)
        elif choice == '5':
            name = Input.stdin('Level: ')
            if not Error_Res.judgeInKeys(name, content.keys()):
                print('You have no such item!')
                sleep(1)
                continue
            if not Error_Res.judgeDictType(content[name]):
                print('Latest level!')
                sleep(1)
                continue
            modify_dict(content[name], bookname+'_'+name, level + 1)
        elif choice == '7':
            saveAsPlain(content, bookname)
            sleep(1)
        elif choice == '8':
            break
        else:
            Error_Res.wrongInput()


def modify(cipherBook):
    modify_dict(cipherBook.content, cipherBook.name)
