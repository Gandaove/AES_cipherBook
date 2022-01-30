# Define file's op
import Input
import Error_res
import Security
from time import sleep


def readCipher(fileName):                               # Read and write
    try:
        with open(fileName, 'r', encoding='utf-8') as f:
            cipherBook = f.readlines()
        return cipherBook
    except (FileNotFoundError, PermissionError, OSError):
        Error_res.wrongFile()


def writeCipher(path, question, key_input_SHA, content):
    try:
        with open(path, 'w', encoding='utf-8') as f1:
            f1.write(question + '\n')
        with open(path, 'a', encoding='utf-8') as f2:
            f2.write(key_input_SHA + '\n')
            f2.write(content)
    except (FileNotFoundError, PermissionError, OSError):
        Error_res.wrongFile()


def saveChange(content, key_input, path, question):
    if key_input == 'None':
        print('Key Empty!' + '\n' + 'Change not save!')
        sleep(1.5)
    else:
        while True:
            saveBool = Input.stdin('Do you want to save your changes? (y/n) ')
            if saveBool == 'y':
                key_input_byte, iv_input = Security.hash_crypt(key_input)
                content = Security.encrypt_AES(
                    key_input_byte, iv_input, str(content))
                writeCipher(path, question, Security.hash_verify(
                    key_input), content)
                print('Changes saved!')
                sleep(1)
                break
            elif saveBool == 'n':
                print('Changes not saved!')
                sleep(1)
                break
            else:
                Error_res.wrongInput()
