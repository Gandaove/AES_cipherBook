import base64
import hashlib
import os
import time
from Crypto.Cipher import AES


def wrongInput():
    print('Wrong input!!!!')
    time.sleep(1)


def quitProgram():
    os.system('pause')
    exit()


def deleteFile(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
        print('Oops, your file just fucked up (^v^)')
    else:
        print('File does not exist? You SOB!')
        quitProgram()


def readCipher(fileName):                               # Read and write
    if os.path.exists(fileName):
        with open(fileName, 'r') as f:
            cipherBook = f.readlines()
        return cipherBook
    else:
        print('File does not exist!')
        quitProgram()


def writeCipher(path, question, answer_input_SHA, content):
    with open(path, 'w') as f1:
        f1.write(question + '\n')
    with open(path, 'a') as f2:
        f2.write(answer_input_SHA + '\n')
        f2.write(content)


def pkcs7_pad(content, block_size=32):                              # fill up by PKCS7
    padding = block_size - len(content.encode('utf-8')) % block_size
    # print('padding:', padding)
    return content + (chr(padding) * padding)


def pkcs7_unpad(content):
    return content[:-ord(content[-1:])]


# Encrypt and Decrypt by AES (CBC)
def encrypt_AES(key, iv, content):
    try:
        encrypt = AES.new(key, AES.MODE_CBC, iv)        # use CBC
    except:
        return('Init failed!')

    content_pad = pkcs7_pad(content)
    content_pad = content_pad.encode('utf-8')
    AES_encrypt = base64.b64encode(encrypt.encrypt(content_pad)).decode()
    return AES_encrypt


def decrypt_AES(key, iv, content):
    try:
        decrypt = AES.new(key, AES.MODE_CBC, iv)
    except:
        return('Init failed!')

    content = content.encode('utf-8')
    content_decode = base64.b64decode(content)
    try:
        AES_decrypt = decrypt.decrypt(content_decode).decode()
        return pkcs7_unpad(AES_decrypt)
    except UnicodeDecodeError:
        return('Key wrong!')


def updateDic(content):
    name = input('Please enter the name of the account you want to update: ')
    if name in content.keys():
        print('Updating.....')
    else:
        print('Adding.....')
    username = input('Please enter the new username: ')
    password = input('Please enter the new password: ')
    content.update({name: {username: password}})
    print('Account updated!')
    time.sleep(1)
    return content


def deleteDic(content):
    name = input('Please enter the name of the account you want to delete: ')
    if name in content.keys():
        content.pop(name)
        print('Account deleted!')
        time.sleep(1)
        return content
    else:
        print('Sorry, you have no such account!')
        time.sleep(1)


def findDic(content):
    print(content.keys())
    name = input('Please enter the name of the account you want to find: ')
    if name in content.keys():
        print(name, ':', content[name])
        os.system('pause')
    else:
        print('Sorry, you have no such account!')
        time.sleep(1)


def showContent(crypt_AES, key_input_byte, iv_input):
    # try:
    concent = decrypt_AES(key_input_byte, iv_input, crypt_AES)
    print(concent)
    time.sleep(1)
    # count = counter(count, path)
    return concent
    # except UnboundLocalError:
    #     print('Error: decrypt failed!')


def MainMenu():
    os.system('cls')
    print('*************Welcome**************')
    print('1.First time use')
    print('2.I already have a cipherBook')
    print('3.Exit')
    choice = input('Please enter your choice: ')
    return choice


def BookMenu():
    os.system('cls')
    print('Warning: Do not open your KEY file when you run this program')
    print('1. Add/Update account')
    print('2. Delete account')
    print('3. Find account')
    print('4. Change Security of cipherBook')
    print('5. Quit Program')
    choice = input('Please enter your choice: ')
    return choice


def SecurityMenu():
    print('a. Change KEY')
    print('b. Change Question')
    print('c. Change Answer')
    choice = input('Please enter your choice: ')
    return choice


def verify():
    count = 8
    path = input('Please input the path of your KEY file: \n')
    while count:
        fileread = readCipher(path)
        question = fileread[0].strip('\n')
        print(question)
        answer_input = input('Please input your answer: \n')
        answer_input_SHA = hashlib.sha256(
            answer_input.encode('utf-8')).hexdigest()
        answer_SHA = fileread[1].strip('\n')
        if answer_SHA == answer_input_SHA:
            print('Answer correct!')
            crypt_AES = fileread[2]
            key_input = input('Please input your key: ')
            key_input_byte = hashlib.sha256(key_input.encode('utf-8')).digest()
            iv_input = hashlib.md5(
                (key_input + answer_input).encode('utf-8')).digest()
            content = showContent(crypt_AES, key_input_byte, iv_input)
            if content == ('Key wrong!'):
                count = counter(count, path)
                continue
            else:
                break
        else:
            print('Answer wrong!')
            count = counter(count, path)
    return content, key_input, answer_input, path, question


def counter(count, path):
    if count == 1:
        print("You don't have chance now!")
        deleteFile(path)
        quitProgram()
    else:
        print('You have', count - 1, 'chance left.', '\n')
        time.sleep(1)
        return count - 1


def optionsFuction(content, key_input, path, question, answer_input):
    # key_input_byte, answer_input_SHA, iv_input = None, None, None
    key_input_byte = hashlib.sha256(key_input.encode('utf-8')).digest()
    answer_input_SHA = hashlib.sha256(answer_input.encode('utf-8')).hexdigest()
    iv_input = None
    while True:
        choice = BookMenu()
        if choice == '1':
            updateDic(content)
        elif choice == '2':
            deleteDic(content)
        elif choice == '3':
            findDic(content)
        elif choice == '4':
            choices = SecurityMenu()
            if choices == 'a':
                key_input = input('Please input your new key: ')
                key_input_byte = hashlib.sha256(
                    key_input.encode('utf-8')).digest()
                print('Key changed!')
                time.sleep(1.5)
            elif choices == 'b':
                question = input('Please input your new question: ')
                print('Question changed!')
                time.sleep(1.5)
            elif choices == 'c':
                answer_input = input('Please input your new answer: ')
                answer_input_SHA = hashlib.sha256(
                    answer_input.encode('utf-8')).hexdigest()
                print('Answer changed!')
                time.sleep(1.5)
        elif choice == '5':           # choose save or not save
            if key_input == 'None' or answer_input == 'None':
                print('Something Empty!')
                print('Changes not saved!')
                time.sleep(1.5)
                break
            else:
                saveBool = input('Do you want to save your changes? (y/n) ')
                if saveBool == 'y':
                    iv_input = hashlib.md5(
                        (key_input + answer_input).encode('utf-8')).digest()
                    content = encrypt_AES(key_input_byte, iv_input, str(content))
                    # break
                    writeCipher(path, question, answer_input_SHA, content)
                    print('Changes saved!')
                    time.sleep(1)
                    # return content, answer_input_SHA, path, question
                    break
                elif saveBool == 'n':
                    print('Changes not saved!')
                    time.sleep(1)
                    break

        else:
            wrongInput()


def firstTime():
    key_dict = {}
    key_input, question, answer_input = 'None', '', 'None'
    # path = ''
    path = input('Please input the path of your KEY file where you want to save: \n')
    print('Warning: You must do(4: a,b,c)')
    time.sleep(3)
    return optionsFuction(key_dict, key_input, path, question, answer_input)


def hadBook():
    content, key_input, answer_input, path, question = verify()
    content = eval(content)
    print(content)
    return optionsFuction(content, key_input, path, question, answer_input)


def main():
    while True:
        choice = MainMenu()
        if choice == '1':
            firstTime()
        elif choice == '2':
            hadBook()
        elif choice == '3':
            decide = input('Are you sure to exit? (y/n)')
            if decide == 'y':
                print('Goodbye!')
                quitProgram()
            elif decide == 'n':
                continue
            else:
                wrongInput()
                continue
        else:
            wrongInput()


if __name__ == '__main__':
    main()
