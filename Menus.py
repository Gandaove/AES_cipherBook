# build console menu
import Input
def MainMenu():
    print('*******AES cipherBook v1.2********')
    print('*************Welcome**************')
    print('1.First time use')
    print('2.I already have a cipherBook')
    print('3.Exit')
    choice = Input.stdin('Please enter your choice: ')
    return choice


def BookMenu():
    print('Warning: Do not open your KEY file when you run this program')
    print('1. Modify Book')
    print('2. Change Security of cipherBook')
    print('3. Back to Main')
    choice = Input.stdin('Please enter your choice: ')
    return choice


def SecurityMenu():
    print('a. Change KEY')
    print('b. Change Question')
    print('c. Back to Opinions')
    choice = Input.stdin('Please enter your choice: ')
    return choice


def ModifyMenu():
    print('1. Add/Update item')
    print('2. Delete item')
    print('3. Print item')
    print('4. Next level')
    print('5. Expand level')
    print('6. Back level')
    choice = Input.stdin('Please enter your choice: ')
    return choice
