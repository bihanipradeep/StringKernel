
import pickle
import Constant as C
from TextProcessing.CsvReader import CsvReader
from Kernel.SubsequenceStringKernel import SubsequenceStringKernel

with open(C.pkl_filename, 'rb') as file:
    clf = pickle.load(file)

csvReader = CsvReader(C.testFile)
X_test = csvReader.getTextTestData()

csvReader = CsvReader(C.inputFile)
X,Y = csvReader.getTextInputData()

SSK = SubsequenceStringKernel(C.N, C.m_lambda, X_test, X)
Z = clf.predict(SSK.getKernel())
print(Z)