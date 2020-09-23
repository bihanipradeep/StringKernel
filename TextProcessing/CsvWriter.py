from numpy import genfromtxt
import numpy as np
from pathlib import Path
import sys

sys.path.append('../')

import Constant as constant
from TextProcessing.CsvReader import CsvReader


class CsvWriter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.outputFile = constant.outputFile

    def get_twitter_data(self):
        csv_reader = CsvReader(self.outputFile)
        tweets = []
        for line in csv_reader.get_lines():
            array_line = line.rstrip().split('"')
            if len(array_line) > 1:
                tweets.append(array_line[1])
        return tweets

    def write_from_old_data(self, party):
        tweets = self.get_twitter_data()
        with open(constant.data_folder + self.file_name, 'a') as fd:
            for tweet in tweets:
                fd.write(party + "," + tweet + "\n")

    def write_to_file(self, data):
        with open(constant.data_folder + self.file_name, 'w') as fd:
            fd.write(data)

    def append_to_file(self, data):
        with open(self.file_name, 'a+') as fd:
            fd.write(data)

# csvwriter = CsvWriter(C.testFile)
# print(csvwriter.write(C.REPUBLICAN))
