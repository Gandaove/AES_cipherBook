# deal with error and judge type...
from File import Value
from pathlib import Path
from os import system
from sys import exit as Exit
from time import sleep
from MySQLdb import OperationalError
from functools import wraps


def handle_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UnboundLocalError:           # AES init failed
            return ('Init failed!')
        except UnicodeDecodeError:          # AES key wrong
            return ('Key wrong!')
        except (FileNotFoundError, PermissionError, OSError):       # file not found
            wrongFile()
        except TypeError:                   # (When reading from file...)read Nonetype
            return ('Creating a new book...')
        except OperationalError:
            wrongConnect()
        except AttributeError:              # ...Not create Attribute...
            return
    return wrapper


def judgeNotNone(value):                # judge if the input is null, give a hint
    if not value:
        print('This Value is empty!')
        return False
    return True


def judgeDictType(value):              # judge if is dict
    return isinstance(value, dict)


def judgeValueType(value):              # judge if is dict
    return isinstance(value, Value)


def judgeInKeys(value, keys):
    return value in keys


def fileExist(file):
    return Path(file).is_file()


def dirExist(path):
    return Path(path).is_dir()


def wrongInput():
    print('Wrong input!!!!')
    sleep(1.5)


def wrongFile():
    print('No such a file...')
    sleep(1)


def wrongConnect():
    print("Wrong sql's user or pwd...")
    sleep(1)


def quitProgram():
    pauseProgram()
    Exit()


def clearScreen():
    system('cls')


def pauseProgram():
    system('pause')
