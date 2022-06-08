# add data to mysql
# change to mysqlclient(MySQLdb)
import MySQLdb
import Security
import book
import Error_res
from time import sleep


class BookSQL(book.Book):                       # basic class
    @Error_res.handle_exception
    def __init__(self):
        super().__init__()
        self._user = 'bookuser'
        self._pwd = 'cipherbook'
        # self._host = '192.168.18.135'
        self._host = 'localhost'
        self.connect = MySQLdb.connect(
            host=self._host, user=self._user, password=self._pwd, port=3306, charset='utf8')
        self.cursor = self.connect.cursor()

        self.connect.select_db('cipherBook')

    @Error_res.handle_exception
    def savetosql(self):
        # check if bookname exist in sql
        if not self.checksql(self._name):
            insert = "insert into BookList(bookname, question, key_hash, content) values('{}', '{}', '{}', '{}')".format(
                self._name, self._question, self._key_input, self._content)
            self.cursor.execute(insert)
            self.connect.commit()               # rollback?
            print("Saved!")
        else:
            print("Bookname already exist, updating...")
            self.updatetosql(self.name)

    def readfromsql(self, name):
        select = "select * from BookList where bookname = '{}'".format(name)
        self.cursor.execute(select)
        data = self.cursor.fetchall()
        self._question = data[0][1]
        self._key_input = data[0][2]
        self._content = data[0][3]
        self._name = data[0][0]

    @Error_res.handle_exception
    def write_file(self, path):
        with open(path, 'w', encoding='utf-8') as f1:
            f1.write(self._question + '\n')
        with open(path, 'a', encoding='utf-8') as f2:
            f2.write(self._key_input + '\n')
            f2.write(self._content)

    def checksql(self, name):
        select_data = 'select bookname from BookList'
        self.cursor.execute(select_data)
        data = self.cursor.fetchall()
        for i in data:
            if i[0] == name:
                return True
        return False

    @Error_res.handle_exception
    def deletefromsql(self, name):
        delete = "delete from BookList where bookname = '{}'".format(name)
        if self.verify(name):
            self.cursor.execute(delete)
            self.connect.commit()
            print("Delete success!")
        else:
            print("Wrong password!")

    @Error_res.handle_exception
    def updatetosql(self, name):
        update = "update BookList set name = '{}', set content = '{}', question = '{}', key_hash = '{}' where bookname = '{}'".format(
            name, self._content, self._question, self._key_input, self._name)
        if self.verify(name):
            self.cursor.execute(update)
            self.connect.commit()
            print("Update success!")
        else:
            print("Wrong password!")
    
    def getKeyOnSQL(self, name):
        select_key = "select key_hash from BookList where bookname = '{}'".format(name)
        self.cursor.execute(select_key)
        return self.cursor.fetchone()[0]

    def verify(self, name):       # Override
        passwd = Security.hash_verify(input("Please input the password: "))
        if self.getKeyOnSQL(name) == passwd:
            return True
        else:
            return False

    def copy_book(self, book):
        self.question = book.question
        self.key_input = Security.hash_verify(book.key_input)
        self.content = Security.pack(book.content, book.key_input)
        self.name = book.name

    def close(self):
        self.cursor.close()
        self.connect.close()


class BookFileToSQL(BookSQL, book.BookFromFile):
    @Error_res.handle_exception
    def __init__(self):
        super().__init__()
        self.run()


def saveToSQL():
    # try:
    data = BookFileToSQL()
    # except (sql.pymysql.OperationalError):
    #     Error_res.wrongConnect()
    #     return
    # data.copy_book()
    data.savetosql()
    data.close()
    sleep(1)


def updateToSQL():
    data = BookFileToSQL()
    name = input("Please input the book name you want to update: ")
    if data.checksql(name):
        data.updatetosql(name)
    else:
        print("This book doesn't exist!")
    data.close()
    sleep(1.5)


def deleteFromSQL():
    data = BookSQL()
    name = input("Please input the book name you want to delete: ")
    if data.checksql(name):
        data.deletefromsql(name)
    else:
        print("This book doesn't exist!")
    data.close()
    sleep(1.5)


def saveToFile():
    data = BookSQL()
    name = input("Please input the book name you want to save: ")
    if data.checksql(name):
        data.readfromsql(name)
        path = input("Please input the path you want to save: ")
        if path:
            data.write_file(path)
            print("Saved!")
        else:
            print("Wrong path!")
    else:
        print("This book doesn't exist!")
    data.close()
    sleep(1.5)
