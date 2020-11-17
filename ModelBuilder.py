# coding: utf-8
from Kernel.SubsequenceStringKernel import SubsequenceStringKernel
from sklearn import svm
import sys
import Util.Util as Util
import numpy as np


def build_model(case_name, m_lambda, n, purpose):
    print("started")
    x, y = Util.get_data(case_name, purpose)
    ssk = SubsequenceStringKernel(n, m_lambda, x, x)
    clf = svm.SVC(kernel='precomputed')
    k = ssk.build_kernel(case_name)
    clf.fit(k, y)
    y_predict = clf.predict(k)
    print(y_predict)
    Util.print_model(case_name, m_lambda, n, clf)
    Util.print_reports(
        case_name, y, y_predict, m_lambda, n, purpose)


if __name__ == "__main__":
    Util.different_parameters(sys.argv[1], build_model, "input")

