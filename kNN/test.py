from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

from kNN import *

# datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
#
# print(datingLabels[0:20])
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# # ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2])
# ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0*array(datingLabels), 15.0*array(datingLabels))
# plt.show()

# normMat, ranges, minVals = autoNorm(datingDataMat)
# print(normMat, ranges, minVals)

def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    print(normMat[0, :])
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 4)
        print("the classifier came back with: %d, the real answer is : %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]) : errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))

# datingClassTest()


def handwritingClassTest():
    hwLabels = []
    traingFileList = listdir('digits/trainingDigits')  # Return a list containing the names of the entries
    m = len(traingFileList)                            # in the directory given by path.
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = traingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('digits/trainingDigits/%s' % fileNameStr)
    testFileList = listdir('digits/testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 4)
        print("the classifier came back with: %d, the real answer is : %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr) : errorCount += 1.0
    print("\nthe total number of errors is : %d" % errorCount)
    print("\nthe total error rate is : %f" % (errorCount/float(mTest)))


# testVector = img2vector('digits/trainingDigits/0_13.txt')
# print(testVector[0, 0:31])
# print(testVector[0, 32:63])

handwritingClassTest()