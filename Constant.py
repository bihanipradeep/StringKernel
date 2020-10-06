base_folder = "/Users/pradeep/Files/ML/StringKernel/"
model_folder = base_folder + "Model/"
data_folder = base_folder + "data/"
input_folder = data_folder + "input/"
result_folder = data_folder + "result/"
test_folder = data_folder + "test/"
inputFile = "input.csv"
inputFile_0 = "/input_0.csv"
inputFile_1 = "/input_1.csv"
testFile_0 = "/test_0.csv"
testFile_1 = "/test_1.csv"
testFile = "test.csv"
outputFile = "BidenTweet.csv"

REPUBLICAN = "0"
DEMOCRATS = "1"
N = 5
m_lambdas = [0.1]
NValues = [1]

cases = {
    "case1": {
        0: "English",
        1: "Turkish"
    },
    "case2": {
        0: "Tweet",
        1: "Shakespeare"
    },
    "case3": {
        0: "Trump",
        1: "Biden"
    }
}
