# build console menu
import Input


def MainMenu():
    print("*******AES cipherBook v1.5********")
    print("*************Welcome**************")
    print("1. First time use")
    print("2. I already have a cipherBook")
    print("3. Operate database")
    print("4. Exit")
    return Input.stdin("Please enter your choice: ")


def BookMenu():
    print("Warning: Do not open your KEY file when you run this program")
    print("1. Modify Book")
    print("2. Change Security of cipherBook")
    print("3. Back to Main")
    return Input.stdin("Please enter your choice: ")


def SecurityMenu():
    print("a. Change KEY")
    print("b. Change Question")
    print("c. Change book's name")
    print("d. Back to Opinions")
    return Input.stdin("Please enter your choice: ")


def ModifyMenu():
    print("1. Add/Update item")
    print("2. Change item's name")
    print("3. Delete item")
    print("4. Print item")
    print("5. Next level")
    print("6. Expand level")
    print("7. Save as plaintext")
    print("8. Back level")
    return Input.stdin("Please enter your choice: ")


def MySQLMenu():
    print("1. Save to database")
    print("2. Delete from database")
    print("3. Save to File")
    print("4. Back to Main")
    return Input.stdin("Please enter your choice: ")
