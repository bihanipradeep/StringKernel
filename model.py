
import pickle
import Constant as C
from TextProcessing.CsvReader import CsvReader
from Kernel.SubsequenceStringKernel import SubsequenceStringKernel
import numpy as np
with open(C.pkl_filename, 'rb') as file:
    clf = pickle.load(file)

csvReader = CsvReader(C.testFile)
X_test = csvReader.getTextTestData()

csvReader = CsvReader(C.inputFile_0)
X = csvReader.getTextTestData()

csvReader = CsvReader(C.inputFile_1)
X1 = csvReader.getTextTestData()
X = np.append(X, X1)
length = X.shape[0]
SSK = SubsequenceStringKernel(C.N, C.m_lambda, X_test, X.reshape(length, 1))
Z = clf.predict(SSK.getKernel())
print(Z)