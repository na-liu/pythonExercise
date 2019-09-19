import matplotlib.lines as mlines
import matplotlib.pyplot as plt  # 绘制散点图
import numpy as np
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置rc参数显示中文
plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示字符

'''
处理输入格式问题file2matrix
Parameters:
    filename: 文件路径
Returns:
    returnMat: 从文件中读取的三个条件的数据，即样本
    classLabelVector: 从文件读取的相应的喜爱程度，即类别
'''


def file2matrix(filename):
    fr = open(filename)  # 打开文件
    arrayOLines = fr.readlines()  # 按行读取文件，list形式
    numberOfLines = len(arrayOLines)  # 得到文件行数：1000
    returnMat = np.zeros((numberOfLines, 3))  # 创建一个numberOfLines行,3列的零数组，用于存储每一行的三项指标
    classLabelVector = []  # 返回的分类标签向量，用于存储每一行对应的类别
    index = 0  # 行的索引值
    for line in arrayOLines:
        # s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        line = line.strip()
        # 使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
        listFromLine = line.split('\t')
        # 将数据前三列提取出来,存放到returnMat的NumPy矩阵中,也就是特征矩阵
        returnMat[index, :] = listFromLine[0:3]  # index为行坐标，列由其后填充即可
        # 根据文本中标记的喜欢的程度进行分类,1代表不喜欢,2代表魅力一般,3代表极具魅力
        if listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        index += 1
    return returnMat, classLabelVector


'''
数据归一化autoNorm
Parameters:
    dataSet - 特征矩阵
Returns:
    normDataSet - 归一化后的特征矩阵
    ranges - 数据范围
    minVals - 数据最小值
'''


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = (dataSet - minVals) / ranges
    return normDataSet, ranges, minVals


'''
数据可视化showdatas
Parameters:
    dataSet - datingDataMat, datingLabels
Returns:
    无
'''


def showdatas(datingDataMat, datingLabels):
    fig, ax = plt.subplots(2, 2, figsize=(13, 8))
    colors = []
    for i in datingLabels:
        if i == 1:
            colors.append('black')
        if i == 2:
            colors.append('yellow')
        if i == 3:
            colors.append('red')
    ax[0][0].scatter(x=datingDataMat[:, 0], y=datingDataMat[:, 1], c=colors, s=15, alpha=0.5)
    title00 = ax[0][0].set_title('每年获得的飞行常客里程数与玩视频游戏所消耗时间占比')
    ax[0][0].set_xlabel("每年获得的飞行常客里程数")
    ax[0][0].set_ylabel("玩视频游戏所消耗时间占比")
    plt.setp(title00, size=9, weight='bold', color='red')  # 改变文字属性

    ax[0][1].scatter(x=datingDataMat[:, 1], y=datingDataMat[:, 2], c=colors, s=15, alpha=0.5)
    ax[0][1].set_title('玩视频游戏所消耗时间占比与每周消费的冰激淋公升数')
    ax[0][1].set_xlabel("玩视频游戏所消耗时间占比")
    ax[0][1].set_ylabel("每周消费的冰琪淋公升数")

    ax[1][0].scatter(x=datingDataMat[:, 0], y=datingDataMat[:, 2], c=colors, s=15, alpha=0.5)
    ax[0][1].set_title('每年获得的飞行常客里程数与每周消费的冰激淋公升数')
    ax[1][0].set_xlabel("每年获得的飞行常客里程数")
    ax[1][0].set_ylabel("每周消费的冰琪淋公升数")
    # 设置图例
    didntLike = mlines.Line2D([], [], color='black', marker='.', markersize=6, label='didntLike')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.', markersize=6, label='smallDoses')
    largeDoses = mlines.Line2D([], [], color='red', marker='.', markersize=6, label='largeDoses')
    # 添加图例
    ax[0][0].legend(handles=[didntLike, smallDoses, largeDoses])
    ax[0][1].legend(handles=[didntLike, smallDoses, largeDoses])
    ax[1][0].legend(handles=[didntLike, smallDoses, largeDoses])
    plt.show()


'''
kNN简单分类器classify0
Parameters:
    inX: 待分类的测试集，单个样本
    dataSet: 已知类型的训练集
    labels: 训练集对应的类别
    k: kNN算法参数，选择最相似的前k个或者说选择距离最短的前k个
Returns:
    sortedClassCount[0][0] ：测试出来的inX的结果
'''


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # shape[0]表示数组的行数
    # 计算距离
    distances = np.sum((inX - dataSet) ** 2, axis=1) ** 0.5
    # 排序，结果为排好序的元素对应的序号,如[1 5 4 0 3 6 2]
    sortedDistIndicies = distances.argsort()  # 排序
    classCount = {}  # 按照相似度高低分类的字典，即相似集
    # 选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]  # 相似度最大的前k个item的分类
        # classCount.get(voteIlabel, 0) ----> {'A',0}
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 将相似集中数据按照出现次数排序，降序
    # key=operator.itemgetter(1),获得前一个参数每一个item的第1域的值
    sortedClassCount = sorted(classCount.items(), key=lambda x: x[1], reverse=True)  # reverse=True为降序
    return sortedClassCount[0][0]  # 返回inx属于的类别


'''
分类器测试函数datingClassTest
Parameters:
    无
Returns:
    normDataSet - 归一化后的特征矩阵
    ranges - 数据范围
    minVals - 数据最小值
'''


def datingClassTest():
    # 打开的文件名
    filename = 'D:\datingTestSet.txt'
    # 打开并处理数据
    datingDataMat, datingLabels = file2matrix(filename)
    # 数据归一化
    normDataSet, ranges, minVals = autoNorm(datingDataMat)
    # 所有样本的行数
    m = normDataSet.shape[0]
    # 取样本的前10%作为测试集
    numTestVecs = int(m * 0.10)
    # 分类错误计数
    errorCount = 0.0

    for i in range(numTestVecs):
        # 前numTestVecs个数据作为测试集,后m-numTestVecs个数据作为训练集
        classifierResult = classify0(normDataSet[i, :], normDataSet[numTestVecs:m, :],
                                     datingLabels[numTestVecs:m], 4)
        print("分类结果:%d\t真实类别:%d" % (classifierResult, datingLabels[i]))
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print("错误率:%f%%" % (errorCount / float(numTestVecs)*100))


"""
函数说明:通过输入一个人的三维特征,进行分类输出

Parameters:
    无
Returns:
    无
"""


def classifyPerson():
    # 输出结果
    resultList = ['讨厌', '有些喜欢', '非常喜欢']
    # 三维特征用户输入
    precentTats = float(input("玩视频游戏所耗时间百分比:"))
    ffMiles = float(input("每年获得的飞行常客里程数:"))
    iceCream = float(input("每周消费的冰激淋公升数:"))
    # 打开的文件名
    filename = "datingTestSet.txt"
    # 打开并处理数据
    datingDataMat, datingLabels = file2matrix(filename)
    # 训练集归一化
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 生成NumPy数组,测试集
    inArr = np.array([precentTats, ffMiles, iceCream])
    # 测试集归一化
    norminArr = (inArr - minVals) / ranges
    # 返回分类结果
    classifierResult = classify0(norminArr, normMat, datingLabels, 3)
    # 打印结果
    print("你可能%s这个人" % (resultList[classifierResult - 1]))


if __name__ == '__main__':
    # classifyPerson()
    datingClassTest()
    # # 打开的文件名
    # filename = 'D:\datingTestSet.txt'
    # # 打开并处理数据
    # datingDataMat, datingLabels = file2matrix(filename)
    # normDataSet, ranges, minVals = autoNorm(datingDataMat)
    # showdatas(datingDataMat, datingLabels)
