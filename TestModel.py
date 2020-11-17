from Kernel.SubsequenceStringKernel import SubsequenceStringKernel
import Util.Util as Util
import sys
import Constant as C
from Model.SVMModel import SVMModel


def test_model(case_name, m_lambda, n, purpose, flag, i):
    clf = Util.read_model(case_name, m_lambda, n)

    if flag:
        x_test = Util.get_data_x(case_name, purpose)
    else:
        x_test, y = Util.get_data_test(case_name, purpose, i)

    x, y1 = Util.get_data(case_name, "input")
    ssk = SubsequenceStringKernel(
        n, m_lambda, x[clf.support_], x_test)
    k = ssk.get_kernel(case_name, clf.support_)

    svm = SVMModel(case_name)

    y_predict = svm.prediction_local(k)
    Util.print_predict(case_name, x_test, y_predict)
    if not flag:
        Util.print_array(
            case_name, m_lambda, n, k, purpose + "_" + str(i))
        Util.print_reports(
            case_name, y, y_predict, m_lambda, n, purpose + "_" + str(i))


if __name__ == "__main__":
    case_name = sys.argv[1]
    flag = len(sys.argv) > 2
    for i in range(1):
        for m_lambda in C.m_lambdas:
            for n in C.NValues:
                test_model(case_name, m_lambda, n, "test", flag, i)

