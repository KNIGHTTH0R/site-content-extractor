__author__ = 'akhil'

class FileWriter:

    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename
        self.file = filepath + '/' + filename

    def setFilePath(self, filepath):
        self._filepath = filepath

    def getFilePath(self):
        return self._filepath

    def setFileName(self, filename):
        self._filename = filename

    def getFileName(self):
        return self._filename

    def setFile(self, file):
        self._file = file

    def getFile(self):
        return self._file

    def writeToFile(self, content):
        file = open(self.file, "a", encoding='utf-8', errors='ignore')
        file.write(content)
        if not content == "\n":
            file.write("\n")
        file.close()

    filepath = property(getFilePath, setFilePath)
    filename = property(getFileName, setFileName)
    file = property(getFile, setFile)

