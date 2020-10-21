import time


def selection_sort(data, drawData, timeTick):
    for i in range(len(data)):
        minIdx = i
        for j in range(i, len(data)):
            drawData(data, getColorArry(len(data), i, j))
            time.sleep(timeTick)
            if data[j] < data[minIdx]:
                minIdx = j
        data[minIdx], data[i] = data[i], data[minIdx]


def getColorArry(dataLen, minIdx, comp):
    colors = []
    for i in range(dataLen):
        if i == minIdx:
            colors.append("blue")
        elif i == comp:
            colors.append("yellow")
        else:
            colors.append("red")
    return colors
