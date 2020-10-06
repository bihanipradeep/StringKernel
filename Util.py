import Constant as C
from TextProcessing.CsvWriter import CsvWriter
import pickle
from sklearn import metrics
import numpy as np
from TextProcessing.CsvReader import CsvReader
import multiprocessing as mp


def get_case_file_name(case_name, m_lambda, n):
    return "_".join([case_name, str(int(m_lambda * 100)), str(n)])


def get_model_file_name(prefix, case_name, m_lambda, n):
    return C.model_folder + case_name + "/" + prefix + get_case_file_name(case_name, m_lambda, n)


def get_result_file_name(case_name, m_lambda, suffix):
    output_file = get_case_file_name(case_name, m_lambda, suffix)
    return get_result_folder(case_name) + output_file


def get_result_folder(case_name):
    return C.result_folder + case_name + "/"


def get_result_header(case_name, m_lambda, n):
    return " ".join([case_name, "lambda:" + str(m_lambda), "N:" + str(n)]) + "\n"


def print_result(case_name, m_lambda, n, reports, y_predict, suffix):
    csv_writer = CsvWriter(get_result_file_name(case_name, m_lambda, suffix))
    csv_writer.append_to_file(get_result_header(case_name, m_lambda, n))
    csv_writer.append_to_file(reports)
    # csv_writer.append_to_file(y_predict.tostring())


def read_model(case_name, m_lambda, n):
    with open(get_model_file_name("pickle_test_", case_name, m_lambda, n), 'rb') as file:
        return pickle.load(file)


def print_model(case_name, m_lambda, n, clf):
    with open(get_model_file_name("pickle_test_", case_name, m_lambda, n), 'wb') as file:
        pickle.dump(clf, file)


def print_array(case_name, m_lambda, n, kernel, purpose):
    with open(get_model_file_name("kernel_" + purpose + "_", case_name, m_lambda, n), 'wb') as file:
        return np.save(file, kernel)


def read_array(case_name, m_lambda, n):
    with open(get_model_file_name("kernel_", case_name, m_lambda, n), 'rb') as file:
        return np.load(file)


def get_kernels(case_name):
    return iterate_cases(case_name, read_array)


def get_models(case_name):
    return iterate_cases(case_name, read_model)


def iterate_cases(case_name, func):
    result = []
    for m_lambda in C.m_lambdas:
        for n in C.NValues:
            result.append(func(case_name, m_lambda, n))
    return result


def different_parameters(case_name, func, purpose):
    for m_lambda in C.m_lambdas:
        for n in C.NValues:
            func(case_name, m_lambda, n, purpose)


def print_reports(case_name, y_actual, y_predict, m_lambda, n, suffix):
    reports = metrics.classification_report(y_actual, y_predict, target_names=C.cases[case_name].values())
    print_result(case_name, m_lambda, n, reports, y_predict, suffix)


def get_file(case_name, purpose):
    if purpose == "input":
        file_name1 = C.input_folder + case_name + C.inputFile_0
        file_name2 = C.input_folder + case_name + C.inputFile_1
    else:
        file_name1 = C.test_folder + case_name + C.testFile_0
        file_name2 = C.test_folder + case_name + C.testFile_1
    return file_name1, file_name2


def get_data(case_name, purpose):
    file_name1, file_name2 = get_file(case_name, purpose)

    csv_reader = CsvReader(file_name1)
    x = csv_reader.get_text_data()
    y = np.array([-1 for _ in range(x.shape[0])])

    csv_reader = CsvReader(file_name2)
    x1 = csv_reader.get_text_data()
    x = np.append(x, x1)
    y = np.append(y, np.array([1 for _ in range(x1.shape[0])]))
    length = x.shape[0]
    return x.reshape(length, 1), y


def read_argument(argv):
    case_name = argv[0]
    m_lambda = float(argv[1])
    n = int(argv[2])
    return case_name, m_lambda, n
