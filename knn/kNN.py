# from numpy import * # 不建议使用，会遇到命名冲突
import numpy as np


# 创建数据集
def createDataSet():
    group = np.array([[1.0, 1.1],
                      [0.9, 0.9],
                      [0, 0],
                      [0.5, 0.6],
                      [1.0, 1.0],
                      [0.8, 0.7],
                      [0, 0.1]])  # 测试集
    labels = ['A', 'A', 'B', 'C', 'A', 'D', 'B']  # 标签集
    return group, labels


'''
kNN简易分类器
Parameters:
    inX: 待分类的测试集
    dataSet: 已知类型的训练集
    labels: 训练集对应的类别
    k: kNN算法参数，选择最相似的前k个或者说选择距离最短的前k个
Returns:
    sortedClassCount[0][0] ：测试出来的inX的结果
'''


# kNN简易分类器
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # shape[0]表示数组的行数
    # 计算距离
    distances = np.sum((inX - dataSet) ** 2, axis=1) ** 0.5
    # 排序，结果为排好序的元素对应的序号,如[1 5 4 0 3 6 2]
    sortedDistIndicies = distances.argsort()  # 排序
    print('sortedDistIndicies:', sortedDistIndicies[0:k])
    classCount = {}  # 按照相似度高低分类的字典，即相似集
    # 选择距离最小的k个点
    for i in range(k):
        print('sortedDistIndicies[%d]:' % i, sortedDistIndicies[i])  # 相似度最大的前k个坐标
        voteIlabel = labels[sortedDistIndicies[i]]  # 相似度最大的前k个item的分类
        print('voteIlabel:', voteIlabel)
        # classCount.get(voteIlabel, 0) ----> {'A',0}
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        print('classCount:', classCount)
    # 将相似集中数据按照出现次数排序，降序
    # key=operator.itemgetter(1),获得前一个参数每一个item的第1域的值
    sortedClassCount = sorted(classCount.items(), key=lambda x: x[1], reverse=True)  # reverse=True为降序
    print('sortedClassCount:', sortedClassCount)
    return sortedClassCount[0][0]  # 返回inx属于的类别


# 主函数
if __name__ == '__main__':
    group, labels = createDataSet()  # 创建数据集
    test = [0.8, 0.9]  # 测试集
    test_class = classify0(test, group, labels, 3)  # kNN分类 todo 标红处什么问题？在另一个文件中引用没有出问题
    print('inX属于%s类' % test_class)

'''
    test.py
    from knn import kNN  # 同包也需要引入
    
    group, labels = kNN.createDataSet()
    print('group', group)
    print('labels', labels)
    print('inX属于%s类' % kNN.classify([0.8, 0.9], group, labels, 3))
'''
'''
    # 计算距离分步计算：
    # diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet  # 将inX复制成4×2的数组，减去测试集
    # print('diffMat:', diffMat)
    # sqDiffMat = diffMat ** 2  # 每个元素平方
    # print('sqDiffMat:', sqDiffMat)
    # sqDistances = sqDiffMat.sum(axis=1)  # 每一行之和
    # print('sqDistances:', sqDistances)
    # distances = sqDistances ** 0.5  # 在上面的基础上开根号
    # print('distances:', distances)
'''
