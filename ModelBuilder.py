# coding: utf-8
from Kernel.SubsequenceStringKernel import SubsequenceStringKernel
from sklearn import svm
import sys
import Util as util
import numpy as np


def build_model(case_name, m_lambda, n, purpose):
    print("started")
    x, y = util.get_data(case_name, purpose)
    ssk = SubsequenceStringKernel(n, m_lambda, x, x)
    clf = svm.SVC(kernel='precomputed')
    k = ssk.build_kernel()
    clf.fit(k, y)
    y_predict = clf.predict(k)
    print(y_predict)
    util.print_model(case_name, m_lambda, n, clf)
    util.print_array(case_name, m_lambda, n, k, purpose)
    util.print_reports(case_name, y, y_predict, m_lambda, n, purpose)


if __name__ == "__main__":
    # case_name, m_lambda, n = util.read_argument(sys.argv[1:])
    # build_model(case_name, m_lambda, n, "input")

    util.different_parameters(sys.argv[1], build_model, "input")
