# deal with error and quit
from os import system
from sys import exit as Exit
from time import sleep
from MySQLdb import OperationalError
# from functools import wraps


def handle_exception(func):
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


def judgeNone(value):                # judge if the input is null, give a hint
    if not value:
        print('Your input is empty!')
        return False
    return True


def judgeDictType(value):              # judge if is dict
    if isinstance(value, dict):
        return True
    return False


def judgeInKeys(value, keys):
    if value in keys:
        return True
    return False


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
    system('pause')
    Exit()
