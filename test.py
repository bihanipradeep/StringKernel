import multiprocessing as mp
import time
import Constant as C
from TextProcessing.CsvReader import CsvReader
from TextProcessing.CsvWriter import CsvWriter

if __name__ == '__main__':
    csv_reader = CsvReader(C.input_folder + "case2/" + "input_1_new_1.csv")
    lines = csv_reader.get_lines()
    texts = []
    text = []
    k = 0
    for line in lines:
        text.append(line.strip())
        if k == 4:
            texts.append("".join(text))
            text=[]
            k = 0
        k+=1
    csv_writer = CsvWriter(C.input_folder + "case2/" + "input_1_new.csv")
    csv_writer.append_to_file("\n".join(texts))