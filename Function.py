# lead functions
import Menus
import Error_res
import Modify_dict
import Security
import File
import Input
from os import system
from time import sleep


def firstTime():
    path = Input.stdin(
        'Please input the path of your KEY file where you want to save: \n')
    if not path:
        Error_res.wrongInput()
        return
    else:
        content = {}
        key_input, question = 'None', ''
        print("Warning: You must Set your Key(Can't be 'None')")
        sleep(3)
        return optionsFuction(content, key_input, path, question)


def hadBook():
    path = Input.stdin('Please input the path of your KEY file: \n')
    if not path:
        Error_res.wrongInput()
        return
    else:
        content, key_input, question = Security.verify(File.readCipher(path))
        if content and key_input:
            key_input_byte, iv = Security.hash_crypt(key_input)
            content = Security.decrypt_AES(key_input_byte, iv, content)
            content = eval(content)
            sleep(1)
            return optionsFuction(content, key_input, path, question)


def optionsFuction(content, key_input, path, question):
    while True:
        system('cls')
        choice = Menus.BookMenu()
        if choice == '1':
            Modify_dict.modify_dict(content, '', 1)
        elif choice == '2':
            key_input, question = Security.secure(key_input, question)
        elif choice == '3':           # choose save or not
            File.saveChange(content, key_input, path, question)
            break
        else:
            Error_res.wrongInput()
