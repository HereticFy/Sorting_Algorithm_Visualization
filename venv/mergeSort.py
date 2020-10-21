import time
from insertionSort import *


def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data, 0, len(data), drawData, timeTick)


def merge_sort_alg(data, left, right, drawData, timeTick):
    if right - left <= 1: return

    middle = left + (right - left) // 2
    merge_sort_alg(data, left, middle, drawData, timeTick)
    merge_sort_alg(data, middle, right, drawData, timeTick)
    merge(data, left, middle, right, drawData, timeTick)


def merge(data, left, middle, right, drawData, timeTick):
    tmp = []
    i = left
    j = middle

    while i < middle and j < right:
        if data[i] <= data[j]:
            tmp.append(data[i])
            i += 1
        else:
            tmp.append(data[j])
            j += 1

    while i < middle:
        tmp.append(data[i])
        i += 1

    while j < right:
        tmp.append(data[j])
        j += 1

    for tmp_index, index in enumerate(range(left, right)):
        data[index] = tmp[tmp_index]

    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)


def getColorArray(length, left, middle, right):
    colorArray = []

    for i in range(length):
        if i >= left and i <= right:
            if i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("pink")
        else:
            colorArray.append("white")
    return colorArray


'''
归并排序有两种优化方法：

1：像快排的优化一样，在数组比较小的时候用插入排序，减少递归 

2：每次归并前对于左边最后一个数和右边第一个数比较，如果左边最后一个数小于右边第一个数则直接合并

先来写第一种优化，只需要重写merge_sort_alg即可
'''


def merge_sort_alg2(data, left, right, drawData, timeTick):
    if right - left <= 1: return

    if right - left < 10:
        insertion_sort_quick(data)
    else:
        middle = left + (right - left) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick)
        merge_sort_alg(data, middle, right, drawData, timeTick)
        merge(data, left, middle, right, drawData, timeTick)


'''
版本3：只需要重写merge即可
'''


def merge2(data, left, middle, right, drawData, timeTick):
    tmp = []
    i = left
    j = middle
    if data[middle-1] < data[middle]:
        return
    else:
        while i < middle and j < right:
            if data[i] <= data[j]:
                tmp.append(data[i])
                i += 1
            else:
                tmp.append(data[j])
                j += 1
    
        while i < middle:
            tmp.append(data[i])
            i += 1
    
        while j < right:
            tmp.append(data[j])
            j += 1

        for tmp_index, index in enumerate(range(left, right)):
            data[index] = tmp[tmp_index]

    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)