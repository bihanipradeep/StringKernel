
from numpy import genfromtxt
import numpy as np

class CsvReader:
    def __init__(self, filename):
        self.fileName = filename
    
    def getTextData(self):
        X = []
        Y = []
        fileRead = open(self.fileName, 'r') 
        lines = fileRead.readlines() 

        for line in lines:
            arryline = line.rstrip().split(',')
            X.append("".join(arryline[1:]))
            Y.append(int(arryline[0]))
        return np.array(X).reshape((len(X), 1)) ,  np.array(Y)
