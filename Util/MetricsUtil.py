from Util import Util as util
import glob
from TextProcessing.CsvReader import CsvReader
import numpy as np
from Model.SVMModel import SVMModel
from Util.KernelUtil import KernelUtil
import Constant as C


def get_input_result_files(case_name):
    return glob.glob(util.get_result_folder(case_name) + "**input")


def get_test_result_files(case_name):
    return glob.glob(util.get_result_folder(case_name) + "**test_?")


def get_header_metrics(texts):
    ns = []
    m_lambda = texts[0].split(" ")[1].split(":")[1]
    for text in texts:
        header_array = text.split(" ")
        n = header_array[2].split(":")[1]
        ns.append(int(n.strip()))
    return m_lambda, ns


def get_precision_row(texts):
    precisions = []
    recalls = []
    f1s = []
    support = []
    for text in texts:
        precision_array = text.strip().split("     ")
        precisions.append(float(precision_array[1].strip()))
        recalls.append(float(precision_array[2].strip()))
        f1s.append(float(precision_array[3].strip()))
        support.append(int(precision_array[4].strip()))
    return precisions[0], recalls[0], f1s[0], support[0]


def gt_f1_row(texts):
    f1s = []
    for text in texts:
        precision_array = text.split("     ")
        f1s.append(float(precision_array[4].strip()))
    return f1s


def get_metrics_data(case_name, purpose):
    if purpose == "input":
        files_input = get_input_result_files(case_name)
    else:
        files_input = [util.get_result_file_name(case_name, C.m_lambda, purpose)]
    metrics = []
    for f in files_input:
        reader = CsvReader(f)
        texts = reader.get_lines()
        m_lambda, ns = get_header_metrics(texts[::9])

        precision1, recall1, f1_1, support1 = get_precision_row(texts[3::9])
        precision2, recall2, f1_2, support2 = get_precision_row(texts[4::9])
        svm = SVMModel(case_name)
        support_count = svm.get_support_vector_count()
        metric = {
            "m_lambda": m_lambda,
            "ns": ns,
            "Data1": support1,
            "Data2": support2,
            "precision1": precision1,
            "precision2": precision2,
            "recall1": recall1,
            "recall2": recall2,
            "f1_1": f1_1,
            "f1_2": f1_2,
            "support1": support_count[0],
            "support2": support_count[1]
        }
        metrics.append(metric)
    return sorted(metrics, key=lambda k: k['m_lambda'])


def get_distance_f1_score(case_name, purpose):
    x, y_actual = util.get_data(case_name, purpose)
    k = get_kernel(case_name, purpose)
    distance, predict = get_distance_predict(
        case_name, purpose)
    positive = distance[y_actual > 0]
    negative = distance[y_actual < 0]

    true_positive = np.sum(positive[positive > 0])
    false_negative = -np.sum(positive[positive < 0])
    false_positive = np.sum(negative[negative > 0])
    f1_1 = (2 * true_positive) / (
            2 * true_positive + false_positive + false_negative)

    true_positive = -np.sum(negative[negative < 0])
    false_negative = np.sum(negative[negative > 0])
    false_positive = -np.sum(positive[positive < 0])
    f1_2 = (2 * true_positive) / (
            2 * true_positive + false_positive + false_negative)
    return f1_1, f1_2


def get_mean(case_name, purpose):
    distance, predict = get_distance_predict(case_name, purpose)
    x, y_actual = util.get_data(case_name, purpose)
    positive = distance[y_actual > 0]
    negative = distance[y_actual < 0]
    return np.mean(positive[positive > 0]
                   ), -np.mean(negative[negative < 0])


def get_mean_ratio(case_name, purpose):
    x, y_actual = util.get_data(case_name, purpose)
    positive, negative = get_classes_distance(y_actual, case_name, purpose)
    m1, m2 = np.mean(positive), -np.mean(negative)
    distance, prediction = get_distance_predict(case_name, purpose)
    return np.divide(distance[y_actual > 0], m1
                     ), np.divide(distance[y_actual < 0], m2)


def get_classes_distance(y_actual, case_name, purpose):
    distance, predict = get_distance_predict(case_name, purpose)
    positive = distance[y_actual > 0]
    negative = distance[y_actual < 0]
    return positive[positive > 0], negative[negative < 0]


def get_distance_predict(case_name, purpose):
    k = get_kernel(case_name, purpose)
    svm = SVMModel(case_name)
    return svm.decision_function_local(k), svm.prediction_local(k)


def get_kernel(case_name, purpose):
    kernel_util = KernelUtil(case_name, purpose)
    kernel = kernel_util.get_kernel()
    return kernel
