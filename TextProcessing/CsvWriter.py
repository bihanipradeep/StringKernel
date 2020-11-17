import sys

sys.path.append('../')
import Constant as constant


class CsvWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, data):
        with open(constant.data_folder + self.file_name, 'w') as fd:
            fd.write(data)

    def append_to_file(self, data):
        with open(self.file_name, 'a+') as fd:
            fd.write(data)
