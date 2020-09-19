
from numpy import genfromtxt
import numpy as np
from pathlib import Path
import sys
sys.path.append('../')

import Constant as C
from TextProcessing.CsvReader import CsvReader

class CsvWriter:
    def __init__(self, filename):
        self.fileName = filename
        self.outputFile = C.outputFile

    def getTweetData(self):
        csvReader = CsvReader(self.outputFile)
        tweets = []
        for line in csvReader.getLines():
            arryline = line.rstrip().split('"')
            if len(arryline) > 1:
                tweets.append(arryline[1])
        return tweets
    
    def write(self, party):
        tweets = self.getTweetData()
        print(tweets)
        with open(C.data_folder + self.fileName,'a') as fd:
            for tweet in tweets:
                fd.write(party + "," + tweet+"\n")

csvwriter = CsvWriter(C.testFile)
print(csvwriter.write(C.REPUBLICAN))



        
