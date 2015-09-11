__author__ = 'akhil'

from os import walk

class InputReader:

    def __init__(self, basepath):
        self._setBasePath(basepath)
        self._setCounter(0)
        self._setFiles()

    def _setBasePath(self, basePath):
        self._basePath = basePath

    def _getBasePath(self):
        return self._basePath

    def _setCounter(self, value):
        self._counter = value

    def _getCounter(self):
        return self._counter

    def _setFiles(self):
        self._files = []
        for (dirpath, dirnames, filenames) in walk(self.basepath):
            self._files.extend(filenames)
            break
        self._files = list(filter(lambda x: not x.startswith('.'), self._files))

    def _getFiles(self):
        return self._files

    basepath = property(_getBasePath, _setBasePath)
    counter = property(_getCounter, _setCounter)
    files = property(_getFiles, _setFiles)

    def hasNextFile(self):
        return self.counter < len(self.files)

    def getNextFile(self):
        if self.counter >= len(self.files):
            return None
        self.counter = self.counter+1
        return self._getFiles()[self.counter-1]
