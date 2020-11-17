from TextProcessing.CsvReader import CsvReader
from TextProcessing.CsvWriter import CsvWriter
from Constant import base_folder

csvReader = CsvReader(base_folder + "text")

text_line = []
final_line = []
k = 0
for line in csvReader.get_lines():
    k += 1
    text_line.append(line.strip())
    if k % 4 == 0:
        k = 0
        final_line.append(" ".join(text_line))
        text_line=[]

csvWriter = CsvWriter(base_folder + "text_modify")
csvWriter.append_to_file("\n".join(final_line))
print(final_line)
