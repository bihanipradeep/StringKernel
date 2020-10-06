import Util as util
import glob
from TextProcessing.CsvReader import CsvReader
import numpy as np


def get_input_result_files(case_name):
    return glob.glob(util.get_result_folder(case_name) + "**input")


def get_test_result_files(case_name):
    return glob.glob(util.get_result_folder(case_name) + "**test")


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
    for text in texts:
        precision_array = text.split("     ")
        precisions.append(float(precision_array[2].strip()))
    return precisions


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
        files_input = get_test_result_files(case_name)
    metrics = []
    for f in files_input:
        reader = CsvReader(f)
        texts = reader.get_lines()
        m_lambda, ns = get_header_metrics(texts[::9])
        precision1 = get_precision_row(texts[3::9])
        precision2 = get_precision_row(texts[4::9])
        f1 = get_precision_row()
        metric = {
            "m_lambda": m_lambda,
            "ns": ns,
            "precision1": precision1,
            "precision2": precision2
        }
        metrics.append(metric)
    return sorted(metrics, key=lambda k: k['m_lambda'])


# Clf: model
# k : kernel matrix to test
def get_decision_function(clf, k):
    y_ = []
    support_ = clf.support_
    dual_coef_ = clf.dual_coef_[0]
    intercept_ = clf.intercept_[0]
    for i in range(len(k)):
        svk = k[i][support_]
        y_.append(svk.dot(dual_coef_.T) + intercept_)
    return y_


def get_distance_decision_line(clf, k):
    return clf.decision_function(clf, k)


def get_distance_f1_score(y_actual, clf, k):
    distance = clf.decision_function(k)
    positive = distance[y_actual > 0]
    negative = distance[y_actual < 0]

    true_positive = np.sum(positive[positive > 0])
    false_negative = -np.sum(positive[positive < 0])
    false_positive = np.sum(negative[negative > 0])
    f1_1 = (2 * true_positive) / (2 * true_positive + false_positive + false_negative)

    true_positive = -np.sum(negative[negative < 0])
    false_negative = np.sum(negative[negative > 0])
    false_positive = -np.sum(positive[positive < 0])
    f1_2 = (2 * true_positive) / (2 * true_positive + false_positive + false_negative)
    return f1_1, f1_2
