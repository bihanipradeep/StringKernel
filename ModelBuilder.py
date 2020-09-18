# coding: utf-8
from Kernel.SubsequenceStringKernel import SubsequenceStringKernel
from TextProcessing.CsvReader import CsvReader
from sklearn import svm
import pickle
import Constant as C

csvReader = CsvReader(C.inputFile)
N = 5
m_lambda = 0.5
X, Y = csvReader.getTextInputData()

SSK = SubsequenceStringKernel(C.N, C.m_lambda, X, X)
clf = svm.SVC(kernel='precomputed')
K = SSK.getKernel()
clf.fit(K, Y)

with open(C.pkl_filename, 'wb') as file:
    pickle.dump(clf, file)

