import multiprocessing as mp
import time
import sys
sys.path.append('../../')
from TextProcessing.CsvReader import CsvReader
from TextProcessing.CsvWriter import CsvWriter

if __name__ == '__main__':
    base_folder = "/Users/pradeep/Files/ML/StringKernel/"
    model_folder = base_folder + "Model/"
    data_folder = base_folder + "data/"
    input_folder = data_folder + "input/"
    csv_reader = CsvReader(input_folder + "case2/" + "input_1_new_1.csv")
    lines = csv_reader.get_lines()
    texts = []
    text = []
    k = 0
    for line in lines:
        text.append(line.strip())
        if k == 3:
            texts.append("".join(text))
            text=[]
            k = 0
        k+=1
    csv_writer = CsvWriter(input_folder + "case2/" + "input_1_new.csv")
    csv_writer.append_to_file("\n".join(texts))