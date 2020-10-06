from Kernel.SubsequenceStringKernel import SubsequenceStringKernel
import Util as Util
import sys
import Constant as C
import numpy as np


def model(case_name, m_lambda, n, purpose):
    clf = Util.read_model(case_name, m_lambda, n)
    x_test, y = Util.get_data(case_name, purpose)
    x, y1 = Util.get_data(case_name, "input")
    ssk = SubsequenceStringKernel(n, m_lambda, x_test, x)
    k = ssk.get_kernel()
    Util.print_array(case_name, m_lambda, n, k,purpose)
    print(clf.predict(k))


#
# def print_model_n(case_name):
#     for m_lambda in C.m_lambdas:
#         for n in C.NValues:
#             model(case_name, True, m_lambda, n, "test")


if __name__ == "__main__":
    Util.different_parameters(sys.argv[1], model, "test")
