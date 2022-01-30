# Define security's function, change key or question
import base64
import hashlib
import Menus
import Error_res
import Input
from time import sleep
from os import system
from Crypto.Cipher import AES


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
    except UnboundLocalError:
        return('Init failed!')

    # content_pad = pkcs7_pad(content)
    content_pad = pkcs7_pad(content).encode('utf-8')
    AES_encrypt = base64.b64encode(encrypt.encrypt(content_pad)).decode()
    return AES_encrypt


def decrypt_AES(key, iv, content):
    try:
        decrypt = AES.new(key, AES.MODE_CBC, iv)
    except UnboundLocalError:
        return('Init failed!')

    content = content.encode('utf-8')
    content_decode = base64.b64decode(content)
    try:
        AES_decrypt = decrypt.decrypt(content_decode).decode()
        return pkcs7_unpad(AES_decrypt)
    except UnicodeDecodeError:
        return('Key wrong!')


def hash_crypt(key):
    key_l = list(key)
    iv_l = list(key[: len(key) // 2])
    for member in range(len(key_l)):
        key_l[member] = hashlib.sha512(
            key_l[member].encode('utf-8')).hexdigest()
    for mem in range(len(iv_l)):
        iv_l[mem] = hashlib.sha512(iv_l[mem].encode('utf-8')).hexdigest()
    # key = hashlib.sha256(''.join(key_l).encode('utf-8')).digest()
    # iv = hashlib.md5(''.join(iv_l).encode('utf-8')).digest()
    return hashlib.sha256(''.join(key_l).encode('utf-8')).digest(), hashlib.md5(''.join(iv_l).encode('utf-8')).digest()


def hash_verify(key):
    key_l = list(key)
    for member in range(len(key_l)):
        key_l[member] = hashlib.sha512(
            key_l[member].encode('utf-8')).hexdigest()
    return hashlib.sha256(''.join(key_l).encode('utf-8')).hexdigest()


def verify(fileread):
    # path = input('Please input the path of your KEY file: \n')
    # fileread = File.readCipher(path)
    if fileread:
        while True:
            question = fileread[0].strip('\n')
            print(question)
            key_input = Input.stdin('Please input your Key: \n')
            key_SHA = fileread[1].strip('\n')
            if key_SHA == hash_verify(key_input):
                print('Key correct!')
                break
            else:
                print('Key wrong!', '\n')
        return fileread[2], key_input, question
    else:
        return None, None, None


def secure(key_input, question):
    while True:
        system('cls')
        choices = Menus.SecurityMenu()
        if choices == 'a':
            key_change = Input.stdin('Please input your new key: ')
            if key_change:
                key_input = key_change
                print('Key changed!')
                sleep(1.5)
            else:
                Error_res.wrongInput()
        elif choices == 'b':
            question = Input.stdin('Please input your new question: ')
            print('Question changed!')
            sleep(1.5)
        elif choices == 'c':
            break
        else:
            Error_res.wrongInput()
    return key_input, question
