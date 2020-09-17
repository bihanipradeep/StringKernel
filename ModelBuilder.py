# coding: utf-8
from Kernel.SubsequenceStringKernel import SubsequenceStringKernel
from TextProcessing.CsvReader import CsvReader
from sklearn import svm
import pickle


csvReader = CsvReader("input.csv")
N = 5
m_lambda = 0.5
X, Y = csvReader.getTextData()

SSK = SubsequenceStringKernel(N, m_lambda, 1, X, X)
clf = svm.SVC(kernel='precomputed')
K = SSK.getKernel()
clf.fit(K, Y)

pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(clf, file)

