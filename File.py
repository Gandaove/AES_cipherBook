import sqlite3      # use sqlite3 to save data

types = ('str', 'bytes')

class File():
    def __init__(self):
        self._path, self._name = '', ''
        self._thing = None

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
        self._path = self._path.replace(self._name, name)
        self._name = name
    
    @path.setter
    def path(self, path):
        self._path = path
    
    @thing.setter
    def thing(self, thing):
        self._thing = thing
    
    # @Error_res.handle_exception
    def readFile(self):             # read bytes file
        with open(self._path, 'rb') as f:
            return f.read()
    
    # @Error_res.handle_exception
    def writeFile(self, content):   # write bytes file
        with open(self._path, 'wb') as f:
            f.write(content)


class Value(File):
    def __init__(self):
        super().__init__()
        self._valuetype = ''
    
    @property
    def __dict__(self):
        return {'Value.path': self._path, 'Value.name': self._name, 'Value.thing': self._thing, 'Value.valuetype': self._valuetype}

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
        try:
            filepath = value.replace('/', '\\')        # reunion to windows path '\\'
            self._path = filepath
            self._name = value.rsplit('\\')[-1]      # with suffix
            self._thing = self.readFile()
            self._valuetype = types[1]
        except FileNotFoundError:               # wrong file or just value
            self._thing, self._name = value, value
            self._path = ''
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
        self._path = filepath
        self._name = filepath.rsplit('\\')[-1]
        self._conn = sqlite3.connect(filepath)
        self._cursor = self._conn.cursor()
        self.createTable()