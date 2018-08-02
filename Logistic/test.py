from numpy import *
import logRegres


# dataArr, labelMat = logRegres.loadDataSet()
# print(shape(dataArr), shape(dataArr[0]))
# weights = logRegres.gradAscent(dataArr, labelMat)
# print(weights)
# logRegres.plotBestFit(weights)

# weights = logRegres.stocGradAscent0(array(dataArr), labelMat)
# print(weights)

# weights = logRegres.stocGradAscent1(array(dataArr), labelMat)
#
# logRegres.plotBestFit(weights)

# frTrain = open('horseColicTraining.txt')
# # currentline = frTrain.readline().strip().split('\t')
# #
# # print(type(currentline[1]))

logRegres.multiTest()
# logRegres.colicTest()
# frTest = open('horseColicTest.txt')
# line = frTest.readline()
# currLine = line.strip().split('\t')
# lineArr = []
# for i in range(21):
#     lineArr.append(float(currLine[i]))
#
# print(size(array(w)), size(array(lineArr)))
