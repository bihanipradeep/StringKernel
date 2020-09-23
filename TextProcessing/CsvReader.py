import numpy as np
import Constant as C


class CsvReader:
    def __init__(self, filename):
        self.fileName = filename

    def get_lines(self):
        file_read = open(self.fileName, 'r')
        return file_read.readlines()

    def get_text_input_data(self):
        x = []
        y = []
        for line in self.get_lines():
            array_line = line.rstrip().split(',')
            x.append("".join(array_line[1:]))
            y.append(int(array_line[0]))
        return np.array(x).reshape((len(x), 1)), np.array(y)

    def get_text_data(self):
        x = self.get_lines()
        return np.array(x).reshape((len(x), 1))
