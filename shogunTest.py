import numpy as np
from shogun import StringCharFeatures, RAWBYTE
from shogun import BinaryLabels
from shogun import SubsequenceStringKernel
from shogun import LibSVM
import Util as Util

x, y = Util.get_data("case4", "input")
strings = ["OUR GREAT USA WANTS NEEDS STIMULUS. WORK TOGETHER AND GET IT DONE. Thank you!",
           "Last night reinforced why I got into this race: We are in a battle for the soul of this nation and it’s a battle we must win."]
test = ['bat', 'soon', 'it is your doom', 'i love your cat cart', 'i love loonytoons']
print(strings)
print(list(x))

train_labels = np.array([1, -1, 1, -1, -1, -1, 1])
test_labels = np.array([1, -1, -1, 1])

features = StringCharFeatures(list(x), RAWBYTE)
test_features = StringCharFeatures(test, RAWBYTE)
#
# # 1 is n and 0.5 is lambda as described in Lodhi 2002
sk = SubsequenceStringKernel(features, features, 3, 0.5)
print(sk.get_kernel_matrix())
# # Train the Support Vector Machine
# labels = BinaryLabels(train_labels)
# C = 1.0
# svm = LibSVM(C, sk, labels)
# svm.train()
#
# # Prediction
# predicted_labels = svm.apply(test_features).get_labels()
# print(predicted_labels)
