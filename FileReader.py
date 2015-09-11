__author__ = 'akhil'

import re

class FileReader:

    def setFileName(self, filename):
        self.filename = filename
        if hasattr(self, 'file'):
            self.setFile()

    def setFilePath(self, filepath):
        self.filepath = filepath
        if hasattr(self, 'file'):
            self.setFile()

    def setFile(self):
        self.file = self.filepath + '/' + self.filename

    def __init__(self, filepath, filename):
        self.setFilePath(filepath)
        self.setFileName(filename)
        self.setFile()

    def getFileName(self):
        return self.filename

    def getFilePath(self):
        return self.filepath

    def getFile(self):
        return self.file

    def _getFileContent(self):
        if hasattr(self, '_filecontent'):
            return self._filecontent
        fileptr = open(self.getFile(), 'r', encoding='utf-8', errors='ignore')
        self._filecontent = fileptr.read()
        fileptr.close()
        return self._filecontent

    def checkForContent(self, patternList, startpos, endpos):
        if not hasattr(self, '_filecontent'):
            self._getFileContent()
        for pattern in patternList:
            regObject = re.compile(pattern, flags=re.I|re.M)
            if regObject.search(self._filecontent, startpos, endpos) is None:
                return False

        return True


