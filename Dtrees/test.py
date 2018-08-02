import trees
import treePlotter


myDat, labels = trees.createDataSet()
# print(myDat)
#
# # print(trees.calcShannonEnt(myDat))
# # myDat[0][-1] = 'maybe'
# # print(trees.calcShannonEnt(myDat))
#
# # print(trees.chooseBestFeatureToSplit(myDat))
# # print(myDat)
# myTree = trees.createTree(myDat, labels)
# print(myTree)

# print(treePlotter.retrieveTree(0))
#
# myTree = treePlotter.retrieveTree(0)
# l = treePlotter.getNumLeafs(myTree)
# d = treePlotter.getTreeDepth(myTree)
# print(l, d)

# treePlotter.createPlot(myTree)
# myTree['no surfacing'][3] = 'maybe'
# print(myTree)
# treePlotter.createPlot(myTree)

# print(labels)
# myTree = treePlotter.retrieveTree(0)

# trees.storeTree(myTree, 'classifierStorage.txt')
# myTree = trees.grabTree('classifierStorage.txt')
# print(myTree)
# print(trees.classify(myTree, labels, [1, 0]))
# print(trees.classify(myTree, labels, [1, 1]))

fr = open('lenses.txt', 'r')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]

lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lensesTree = trees.createTree(lenses, lensesLabels)
print(lensesTree)

treePlotter.createPlot(lensesTree)
