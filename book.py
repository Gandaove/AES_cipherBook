# set class 'Book'
import Security
import Input
import Error_Res
import File
import _pickle as pickle                   # file as bin-flow
from time import sleep
from pathlib import Path


class Book(File.File):
    def __init__(self):
        super().__init__()
        self._content, self._key_input, self._question = {}, '', ''     # type --> dict, str, str
        self._suffix = None              # book's suffix, type --> str

    @property
    def content(self):
        return self._content

    @property
    def key_input(self):
        return self._key_input

    @property
    def question(self):
        return self._question
    
    @property
    def name(self):
        return super().name
    
    @name.setter
    def name(self, name):
        self._path = self._path.with_name(self._name + self._suffix)
        self._name = name

    @content.setter
    def content(self, content):
        self._content = content

    @key_input.setter
    def key_input(self, key_input):
        self._key_input = key_input

    @question.setter
    def question(self, question):
        self._question = question


class BookCreate(Book):
    def run(self):
        path = Path(Input.stdin('Please input the path of your KEY file: \n'))
        if not Error_Res.fileExist(path):
            Error_Res.wrongInput()
            return
        self._path = path
        self._name = path.stem
        self._suffix = path.suffix

    def writePreProcess(self):                  # change all File.Value to str
        def traverse(content):
            for key, value in content.items():
                if isinstance(value, File.Value):
                    content[key] = value.__dict__
                elif isinstance(value, dict):
                    traverse(value)
            return content
        self._content = traverse(self._content)
        self._content = Security.pack(
            pickle.dumps(self._content), self._key_input)

    # @Error_res.handle_exception
    def writeBook(self):
        self.writePreProcess()
        super().writeFile(path=self._path, content=Security.b64encode(self._question) + b'\n' +
                          Security.hash_verify(self._key_input) + b'\n'
                          + self._content)

    def saveChange(self):
        if self._key_input == '' or self._question == '':
            print('Key Empty!' + '\n' + 'Change not save!')
            sleep(1.5)
        else:
            while True:
                saveBool = Input.stdin(
                    'Do you want to save your changes? (y/n) ')
                if saveBool == 'y' or saveBool == '':
                    self.writeBook()
                    print('Changes saved!')
                    sleep(1)
                    break
                elif saveBool == 'n':
                    print('Changes not saved!')
                    sleep(1)
                    break
                else:
                    Error_Res.wrongInput()


class BookFromFile(BookCreate):
    @Error_Res.handle_exception
    def run(self):
        super().run()
        if not Error_Res.fileExist(self._path):
            Error_Res.wrongFile()
            print("This is a empty book!")
            return
        cipherBook = self.readBook().splitlines()
        self._question = Security.b64decode(cipherBook[0]).strip(b'\n')
        self._key_input = cipherBook[1].strip(b'\n')
        self._content = cipherBook[2].strip(b'\n')
        self.verify()

    def loadPreProcess(self):                   # change all value to File.Value
        self._content = pickle.loads(
            Security.unpack(self._content, self._key_input))
        valueabc = File.Value()

        def traverse(content):
            for key, value in content.items():
                if Error_Res.judgeDictType(value) and value.keys() == valueabc.__dict__.keys():
                    obj = File.Value()
                    obj.__dict__ = value
                    content[key] = obj
                else:
                    traverse(value)
            return content
        self._content = traverse(self._content)

    @Error_Res.handle_exception
    def readBook(self):
        return super().readFile(path=self._path)  # .decode()

    def verify(self):
        while True:
            print(self._question.decode())
            key_input = Input.stdin('Please input your Key: \n')
            if self._key_input != Security.hash_verify(key_input):
                print('Key wrong!', '\n')
                continue
            print('Key correct!')
            break
        self._key_input = key_input
        # pickle: convert bytes to dict
        self.loadPreProcess()
