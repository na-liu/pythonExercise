import numpy as np


def GetData(datapath):
    Dist = np.zeros((10, 10))
    with open("a.txt") as file:
        data = np.array(file.read().split())
        count = 0
        # print(len(data))
        print(data)
        for i in range(10):
            for j in range(10):
                if data[count] == '0':
                    Dist[i, j] = data[count]
                    count += 1
                    break
                else:
                    Dist[i, j] = data[count]
                    count += 1

    print(Dist)
