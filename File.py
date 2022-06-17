import Error_Res
import sqlite3                  # use sqlite3 to save data
from pathlib import Path


types = ('str', 'bytes')

class File():
    def __init__(self):
        self._path = None       # type --> pathlib.Path
        self._name = None       # type --> str
        self._thing = None      # type --> str or bytes

    @property
    def name(self):
        return self._name
    
    @property
    def path(self):
        return self._path
    
    @property
    def thing(self):
        return self._thing
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @path.setter
    def path(self, path):
        self._path = path
    
    @thing.setter
    def thing(self, thing):
        self._thing = thing
    
    # @Error_Res.handle_exception
    @classmethod
    def readFile(cls, path):             # read bytes file
        with open(path, 'rb') as f:
            return f.read()
    
    # @Error_Res.handle_exception
    @classmethod
    def writeFile(cls, path, content):   # write bytes file
        with open(path, 'wb') as f:
            f.write(content)


class Value(File):
    def __init__(self):
        super().__init__()
        self._valuetype = ''
    
    @property
    def __dict__(self) -> dict:
        return {'Value.path': self._path, 'Value.name': self._name, 'Value.thing': self._thing, 'Value.valuetype': self._valuetype}

    def __repr__(self) -> str:
        return self._name

    @property
    def valuetype(self):
        return self._valuetype
    
    @valuetype.setter
    def valuetype(self, valuetype):
        self._valuetype = valuetype
    
    @__dict__.setter
    def __dict__(self, diction):
        self._path = diction['Value.path']
        self._name = diction['Value.name']
        self._thing = diction['Value.thing']
        self._valuetype = diction['Value.valuetype']

    def create(self, value):                 # filepath or just value
        path = Path(value)
        self._path = path
        if Error_Res.fileExist(path):
            self._name = path.name
            self._thing = self.readFile(path)
            self._valuetype = types[1]
        else:
            self._name, self._thing = value, value
            self._valuetype = types[0]


class File_SQLite(File):
    def __init__(self):
        super().__init__()
        self._conn, self._cursor = None, None
    
    @property
    def conn(self):
        return self._conn
    
    @property
    def cursor(self):
        return self._cursor

    @conn.setter
    def conn(self, conn):
        self._conn = conn
    
    @cursor.setter
    def cursor(self, cursor):
        self._cursor = cursor
    
    def create(self, filepath):
        self._path = Path(filepath)
        self._name = self._path.name
        self._conn = sqlite3.connect(filepath)
        self._cursor = self._conn.cursor()
        self.createTable()
        