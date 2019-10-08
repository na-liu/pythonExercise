# -*- coding: utf-8 -*-
# 	基于贪心算法的旅行商问题解法Python源码
import numpy as np


class Node:
    """
        类名：Node
        类说明：	城市节点类
    """

    def __init__(self, CityNum):
        """
        函数名：GetData()
        函数功能：	从外界读取城市数据并处理
            输入	无
            输出
                    2 CityNum：城市数量
                    3 Dist：城市间距离矩阵
        其他说明：无
        """
        self.visited = [False] * CityNum  # 记录城市是否走过
        self.start = 0  # 起点城市
        self.end = 0  # 目标城市
        self.current = 0  # 当前所处城市
        self.num = 0  # 走过的城市数量
        self.pathsum = 0  # 走过的总路程
        self.lb = 0  # 当前结点的下界
        self.listc = []  # 记录依次走过的城市


def GetData(datapath):
    """
    函数名：GetData()
    函数功能：	从gr48中读取各个城市之间的距离矩阵
        输入	datapath
        输出	1 CityNum：城市数量
                2 Dist：城市间距离矩阵
    """
    CityNum = 48
    Dist = np.zeros((CityNum, CityNum))
    with open(datapath) as file:
        data = np.array(file.read().split())
        count = 0
        print(len(data))
        for i in range(10):
            for j in range(10):
                if data[count] == '0':
                    Dist[i, j] = data[count]
                    count += 1
                    break
                else:
                    Dist[i, j] = data[count]
                    count += 1
    return CityNum, Dist


def ResultShow(Min_Path, BestPath, CityNum, string):
    """
        函数名：GetData()
        函数功能：	从外界读取城市数据并处理
            输入	无
                2 CityNum：城市数量
                3 Dist：城市间距离矩阵
        其他说明：无
    """
    print("基于" + string + "求得的旅行商最短路径为：")
    for m in range(CityNum):
        print(str(BestPath[m]) + "—>", end="")
    print(BestPath[CityNum])
    print("总路径长为：" + str(Min_Path))
    print()
