
from numpy import genfromtxt
import numpy as np
from pathlib import Path


class CsvReader:
    def __init__(self, filename):
        self.fileName = filename

    def getLines(self):
        fileRead = open("data/" + self.fileName, 'r')
        return fileRead.readlines()


    def getTextInputData(self):
        X = []
        Y = []
        for line in self.getLines():
            arryline = line.rstrip().split(',')
            X.append("".join(arryline[1:]))
            Y.append(int(arryline[0]))
        return np.array(X).reshape((len(X), 1)),  np.array(Y)
        
    def getTextTestData(self):
        X = self.getLines()
        return np.array(X).reshape((len(X), 1))
