import Util.Util as Util
import Constant as C
import numpy as np


class SVMModel:
    def __init__(self, case_name):
        self.clf = Util.read_model(case_name, C.m_lambda, C.N)

    def prediction_local(self, k):
        decision = self.decision_function_local(k)
        prediction = []
        for d in decision:
            prediction.append(-1 if d < 0 else 1)
        return np.array(prediction)

    def decision_function_local(self, k):
        kernel = k.T
        dual_coef = self.clf.dual_coef_[0]
        intercept = self.clf.intercept_[0]
        precision = []
        for k_temp in kernel:
            precision.append(np.matmul(k_temp, dual_coef) + intercept)
        return np.array(precision)

    def get_support_vector_count(self):
        return self.clf.n_support_

# print("m_lambda:", m_lambda)
# print("n:", n)
# print(clf.support_)
# print(clf.support_vectors_)
# print(clf.dual_coef_)
# print(clf.n_support_)
# print(clf.intercept_)
# print(clf.classes_)
