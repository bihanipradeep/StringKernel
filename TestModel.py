from Kernel.SubsequenceStringKernel import SubsequenceStringKernel
import Util as Util
import sys
import Constant as C


def test_model(case_name, m_lambda, n, purpose):
    clf = Util.read_model(case_name, m_lambda, n)
    x_test, y = Util.get_data(case_name, purpose)
    x, y1 = Util.get_data(case_name, "input")
    ssk = SubsequenceStringKernel(n, m_lambda, x_test, x)
    k = ssk.get_kernel()
    y_predict = clf.predict(k)
    Util.print_array(case_name, m_lambda, n, k, purpose)
    Util.print_reports(case_name, y, y_predict, m_lambda, n, purpose)


def print_model_n(case_name):
    for m_lambda in C.m_lambdas:
        for n in C.NValues:
            test_model(case_name, True, m_lambda, n, "test")


if __name__ == "__main__":
    Util.different_parameters(sys.argv[1], test_model, "test")
    # print_model_n(sys.argv[1])

# case2 [0 0 1 0 0 1 0 0 0 1 1 1 1 1 1 1 1 1]
# print("-------------------")
# print("m_lambda:", m_lambda)
# print("n:", n)
# print(clf.support_)
# print(clf.support_vectors_)
# print(clf.dual_coef_)
# print(clf.n_support_)
# print(clf.intercept_)
# print(clf.classes_)
