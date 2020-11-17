import Util.Util as Util
import Constant as C


class KernelUtil:
    def __init__(self, case_name, purpose):
        self.case_name = case_name
        if purpose == "input":
            clf = Util.read_model(case_name, C.m_lambda, C.N)
            self.kernel = Util.read_array(
                case_name, C.m_lambda, C.N, purpose)[1][clf.support_]
        else:
            self.kernel = Util.read_array_test(
                case_name, C.m_lambda, C.N, purpose)[0]

    def get_kernel(self):
        return self.kernel


