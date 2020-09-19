# coding: utf-8
from Kernel.SubsequenceStringKernel import SubsequenceStringKernel
from TextProcessing.CsvReader import CsvReader
from sklearn import svm
import pickle
import Constant as C
import numpy as np

csvReader = CsvReader(C.inputFile_0)
X = csvReader.getTextTestData()
Y = np.array([0 for _ in range(X.shape[0]) ])

csvReader = CsvReader(C.inputFile_1)
X1 = csvReader.getTextTestData()
X = np.append(X, X1)
Y = np.append(Y, np.array([1 for _ in range(X1.shape[0])]))
length = X.shape[0]

SSK = SubsequenceStringKernel(C.N, C.m_lambda, X.reshape(length, 1), X.reshape(length, 1))

clf = svm.SVC(kernel='precomputed')
K = SSK.getKernelInput()
print("Kernel Finished !!!")
print(K)
clf.fit(K, Y)

with open(C.pkl_filename, 'wb') as file:
    pickle.dump(clf, file)

