# Security's function, change key or question
import Menus
import Error_res
import Input
from hashlib import sha512, sha256, md5
from base64 import b64encode, b64decode
from time import sleep
from os import system
from Crypto.Cipher import AES


def pkcs7_pad(content, block_size=32):                              # fill up by PKCS7
    padding = block_size - len(content) % block_size
    return content + bytes([padding] * padding)


def pkcs7_unpad(content):
    return content[:-ord(content[-1:])]


# Encrypt and Decrypt by AES (CBC)
@Error_res.handle_exception
def encrypt_AES(key, iv, content):
    encrypt = AES.new(key, AES.MODE_CBC, iv)        # use CBC
    # content_pad = pkcs7_pad(content).encode()
    AES_encrypt = encrypt.encrypt(pkcs7_pad(content))
    return b64encode(AES_encrypt)


@Error_res.handle_exception
def decrypt_AES(key, iv, content):
    decrypt = AES.new(key, AES.MODE_CBC, iv)
    # content = content.encode()
    AES_decrypt = decrypt.decrypt(b64decode(content))
    return pkcs7_unpad(AES_decrypt)


def hash_crypt(key):            # utf-8
    key_l = list(key)
    iv_l = list(key[: len(key) // 2])
    for member in range(len(key_l)):
        key_l[member] = sha512(key_l[member].encode()).hexdigest()
    for mem in range(len(iv_l)):
        iv_l[mem] = sha512(iv_l[mem].encode()).hexdigest()
    # key = hashlib.sha256(''.join(key_l).encode()).digest()
    # iv = hashlib.md5(''.join(iv_l).encode()).digest()
    return sha256(''.join(key_l).encode()).digest(), md5(''.join(iv_l).encode()).digest()


def hash_verify(key):
    key_l = list(key)
    for member in range(len(key_l)):
        key_l[member] = sha512(key_l[member].encode()).hexdigest()
    key_hash = sha256(''.join(key_l).encode()).digest()
    return b64encode(key_hash)


def pack(content, key):
    key_byte, iv = hash_crypt(key)
    content = encrypt_AES(key_byte, iv, content)
    return content


def unpack(content, key):
    key_byte, iv = hash_crypt(key)
    content = decrypt_AES(key_byte, iv, content)
    return content


def security(cipherBook):
    while True:
        system('cls')
        choices = Menus.SecurityMenu()
        if choices == 'a':
            key_change = Input.stdin('Please input your new key: ')
            if not Error_res.judgeNone(key_change):
                Error_res.wrongInput()
                continue
            cipherBook.key_input = key_change
            print('Key changed!')
            sleep(1.5)
        elif choices == 'b':
            cipherBook.question = Input.stdin(
                'Please input your new question: ').encode()
            print('Question changed!')
            sleep(1.5)
        elif choices == 'c':
            name = Input.stdin(
                'Please input your new book name: (no need to add extension)')
            if not Error_res.judgeNone(name):
                Error_res.wrongInput()
                continue
            cipherBook.name = name
            print('Book name changed!')
            sleep(1.5)
        elif choices == 'd':
            break
        else:
            Error_res.wrongInput()
    return cipherBook
