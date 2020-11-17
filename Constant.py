base_folder = "/Users/pradeep/Files/ML/StringKernel/"
model_folder = base_folder + "Model/"
data_folder = base_folder + "data/"
input_folder = data_folder + "input/"
result_folder = data_folder + "result/"
test_folder = data_folder + "test/"
image_folder = base_folder + "img/"
inputFile = "/input.csv"
inputFile_0 = "/input_0.csv"
inputFile_1 = "/input_1.csv"
testFile_0 = "/test_0.csv"
testFile_1 = "/test_1.csv"
testFile = "/test.csv"

REPUBLICAN = "0"
DEMOCRATS = "1"
m_lambda = 0.85
N = 5
m_lambdas = [0.85]
NValues = [5]

trumpImage = "trump.jpg"
bibelImage = "bible.jpeg"
bidenImage = "biden.jpg"
emmanuelImage = "emmanuel.png"
erdoganImage = "erdogan.jpg"
jhonsonImage = "jhonson.jpg"
shakespeareImage = "shakespeare.jpg"

Experiments = {
    "experiment1": "case1",
    "experiment2": "case5",
    "experiment3": "case2",
    "experiment4": "case6",
    "experiment5": "case4",
    "experiment6": "case8",
    "experiment7": "case9"
}

images = {
    "experiment1": {
        0: trumpImage,
        1: erdoganImage
    },
    "experiment2": {
        0: trumpImage,
        1: emmanuelImage
    },
    "experiment3": {
        0: trumpImage,
        1: shakespeareImage
    },
    "experiment4": {
        0: shakespeareImage,
        1: bibelImage
    },
    "experiment5": {
        0: trumpImage,
        1: bidenImage
    },
    "experiment6": {
        0: bidenImage,
        1: bibelImage
    },
    "experiment7": {
        0: trumpImage,
        1: jhonsonImage
    }
}
cases = {
    "case1": {
        0: "Trump",
        1: "Erdogan"
    },
    "case2": {
        0: "Trump",
        1: "Shakespeare"
    },
    "case3": {
        0: "None",
        1: "None"
    },
    "case4": {
        0: "Trump",
        1: "Biden"
    },
    "case5": {
        0: "Trump",
        1: "Macron"
    },
    "case6": {
        0: "Shakespeare",
        1: "Bible"
    },
    "case7": {
        0: "Democrats",
        1: "Republican"
    },
    "case8": {
        0: "Biden",
        1: "Bible"
    },
    "case9": {
        0: "Trump",
        1: "Johnson"
    }
}
