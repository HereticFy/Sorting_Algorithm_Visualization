import time
import random as r
from insertionSort import *

'''
1、快速排序的基本思想：

快速排序使用分治的思想，通过一趟排序将待排序列分割成两部分，其中一部分记录的关键字均比另一部分记录的关键字小。

之后分别对这两部分记录继续进行排序，以达到整个序列有序的目的。

2、快速排序的三个步骤：

(1)选择基准：在待排序列中，按照某种方式挑出一个元素，作为 "基准"（pivot）

(2)分割操作：以该基准在序列中的实际位置，把序列分成两个子序列。此时，在基准左边的元素都比该基准小，在基准右边的元素都比基准大

(3)递归地对两个序列进行快速排序，直到序列为空或者只有一个元素。
'''

'''
版本1：选取尾部元素为基准
'''


def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    # swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]

    return border


def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        # LEFT PARTITION
        quick_sort(data, head, partitionIdx - 1, drawData, timeTick)

        # RIGHT PARTITION
        quick_sort(data, partitionIdx + 1, tail, drawData, timeTick)


def getColorArray(dataLen, head, tail, border, currIdx, isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        # base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray


'''
双指针版本，也是原地快排

每次选取数组第一个元素为基准，用两个指针从头到尾和从尾到头遍历。

每次右边先走，发现比基准大的元素就停下，然后左边开始走，找到比基准大的元素也停下，然后两两换位。

最后当左右指针相遇的时候，用基准元素与此时指针相遇时指向的元素互换即可。这样基准左边的元素都比它小，右边元素都比它大。

然后再对两侧进行递归，知道递归到数组只有一个或者空的时候（在这里我们判断的标准是每次递归之前检查左侧指针是否大于等于右侧指针），数组就是有序的了！
'''


def partition2(data, left, right):
    if left >= right:
        return
    pivot = data[left]
    index_pivot = left
    while left < right:
        while left < right and data[right] >= pivot:
            right -= 1
        while left < right and data[left] <= pivot:
            left += 1
        data[right], data[left] = data[left], data[right]
    data[left], data[index_pivot] = data[index_pivot], data[left]
    return left


def quick_sort_2(data, left, right):
    if left >= right: return
    mid = partition2(data, left, right)

    # left
    quick_sort_2(data, left, mid - 1)

    # right
    quick_sort_2(data, mid + 1, right)


'''
版本3：

我们同样是采用数组的第一个元素作为基准，但是我们采用额外辅助空间来完成这个快排

'''


def partition3(data):
    pivot = data[0]
    left = [elt for elt in data if elt < pivot]
    right = [elt for elt in data if elt > pivot]
    return pivot, left, right


def quick_sort_3(data):
    if len(data) < 2: return data
    pivot, left, right = partition3(data)
    return quick_sort_3(left) + [pivot] + quick_sort_3(right)


'''
版本4 与 5：

在版本2和3的基础上，采用随机选择基准的方法

'''


def partition4(data, left, right):
    if left >= right:
        return
    random_index = r.randint(0, len(data) - 1)
    data[left], data[random_index] = data[random_index], data[left]
    index_pivot = left
    pivot = data[left]
    while left < right:
        while left < right and data[right] >= pivot:
            right -= 1
        while left < right and data[left] <= pivot:
            left += 1
        data[right], data[left] = data[left], data[right]
    data[left], data[index_pivot] = data[index_pivot], data[left]
    return left


def quick_sort_4(data, left, right):
    if left >= right: return
    mid = partition2(data, left, right)

    # left
    quick_sort_2(data, left, mid - 1)

    # right
    quick_sort_2(data, mid + 1, right)


def partition5(data):
    index_pivot = r.randint(0, len(data) - 1)
    pivot = data[index_pivot]
    left = [elt for elt in data if elt < pivot]
    right = [elt for elt in data if elt > pivot]
    return pivot, left, right


def quick_sort_5(data):
    if len(data) < 2: return data
    pivot, left, right = partition5(data)
    return quick_sort_5(left) + [pivot] + quick_sort_5(right)


'''
版本6，7：

在版本2，3的基础上，采用三数取中的方法来决定pivot，即首元素，尾元素，和正中间元素的中值

pivot选取的理想情况是：让分区中比 pivot 小的元素数量和比 pivot 大的元素数量差不多。

较常用的做法是三数取中（ midian of three ），即从第一项、最后一项、中间一项中取中位数作为 pivot。

当然这并不能完全避免最差情况的发生。所以很多时候会采取更小心、更严谨的 pivot 选择方案（对于大数组特别重要）。

比如先把大数组平均切分成左中右三个部分，每个部分用三数取中得到一个中位数，再从得到的三个中位数中找出中位数。

在 javascript v8 引擎中的选择 pivot 的方式：

认为超过1000项的数组是大数组，每隔200左右（不固定）选出一个元素，

从这些元素中找出中位数，再加入首尾两个元素，从这个三个元素中找出中位数作为 pivot。

'''


def partition6(data, left, right):
    if left >= right:
        return
    # select pivot 三数取中, 并且把中位数换到left的位置上
    mid = left + (right - left) // 2
    if data[mid] > data[right]:
        data[mid], data[right] = data[right], data[mid]
    if data[left] > data[right]:
        data[left], data[right] = data[right], data[left]
    if data[mid] > data[left]:
        data[mid], data[left] = data[left], data[mid]

    index_pivot = left
    pivot = data[index_pivot]

    while left < right:
        while left < right and data[right] >= pivot:
            right -= 1
        while left < right and data[left] <= pivot:
            left += 1
        data[right], data[left] = data[left], data[right]
    data[left], data[index_pivot] = data[index_pivot], data[left]
    return left


def quick_sort_6(data, left, right):
    if left >= right: return
    mid = partition6(data, left, right)

    # left                                                                 
    quick_sort_6(data, left, mid - 1)

    # right                                                                
    quick_sort_6(data, mid + 1, right)


def partition7(data):
    # select pivot 三数取中, 并且把中位数换到left的位置上
    left, right = 0, len(data) - 1
    mid = left + (right - left) // 2
    if data[mid] > data[right]:
        data[mid], data[right] = data[right], data[mid]
    if data[left] > data[right]:
        data[left], data[right] = data[right], data[left]
    if data[mid] > data[left]:
        data[mid], data[left] = data[left], data[mid]

    index_pivot = left
    pivot = data[index_pivot]
    left = [elt for elt in data if elt < pivot]
    right = [elt for elt in data if elt > pivot]
    return pivot, left, right


def quick_sort_7(data):
    if len(data) < 2: return data
    pivot, left, right = partition7(data)
    return quick_sort_7(left) + [pivot] + quick_sort_7(right)


'''
优化1、当待排序序列的长度分割到一定大小后，使用插入排序。

原因：对于很小和部分有序的数组，快排不如插排好。当待排序序列的长度分割到一定大小后，继续分割的效率比插入排序要差，此时可以使用插排而不是快排

截止范围：待排序序列长度N = 10，虽然在5~20之间任一截止范围都有可能产生类似的结果，这种做法也避免了一些有害的退化情形。摘自《数据结构与算法分析》Mark Allen Weiness 著

我们在这只示范基于版本6（三数取中原地快排）的版本，且使用快速插入排序

版本8
'''


def partition8(data, left, right):
    if left >= right:
        return
    # select pivot 三数取中, 并且把中位数换到left的位置上
    mid = left + (right - left) // 2
    if data[mid] > data[right]:
        data[mid], data[right] = data[right], data[mid]
    if data[left] > data[right]:
        data[left], data[right] = data[right], data[left]
    if data[mid] > data[left]:
        data[mid], data[left] = data[left], data[mid]

    index_pivot = left
    pivot = data[index_pivot]

    while left < right:
        while left < right and data[right] >= pivot:
            right -= 1
        while left < right and data[left] <= pivot:
            left += 1
        data[right], data[left] = data[left], data[right]
    data[left], data[index_pivot] = data[index_pivot], data[left]
    return left


def quick_sort_8(data, left, right):
    if left >= right: return
    if right - left + 1 < 10:
        insertion_sort_quick(data)
    else:
        mid = partition8(data, left, right)

        # left                                                                 
        quick_sort_8(data, left, mid - 1)

        # right                                                                
        quick_sort_8(data, mid + 1, right)


'''
优化2、在一次分割结束后，可以把与Key相等的元素聚在一起，继续下次分割时，不用再对与key相等元素分割

版本9
在版本8的基础上加入重复元素聚集在中间的操作

这个操作其实很容易理解，我们使用3个指针，分别为 lt，i，gt

初始化 lt = left，gt = right + 1，i = left + 1

当i小于gt时：

1：如果data[i] > pivot：我们交换gt-1和i位置上的元素，确保比pivot大的数排在后面，然后gt-=1

2：如果data[i] < pivot：我们交换lt+1和i位置上的元素，确保比pivot小的数排在前面，然后i+=1 和 lt+=1

3：如果data[i] = pivot：我们只用i+=1 因为一般这个时候i这个指针遍历过的数都是小于等于pivot的，所以只需要继续往前遍历即可

最后交换lt和left位置上的元素

这样我们就能保证，left到lt-1这个区间的元素全部比pivot小

lt到gt-1上的元素全部等于pivot

gt到right上的元素全部大于pivot
'''


def partition9(data, left, right):
    if left >= right:
        return
    # select pivot 三数取中, 并且把中位数换到left的位置上
    mid = left + (right - left) // 2
    if data[mid] > data[right]:
        data[mid], data[right] = data[right], data[mid]
    if data[left] > data[right]:
        data[left], data[right] = data[right], data[left]
    if data[mid] > data[left]:
        data[mid], data[left] = data[left], data[mid]

    index_pivot = left
    pivot = data[index_pivot]

    lt = left  # arr[left+1...lt] < v
    # gt 大于v 部分开始的下标，初始为空
    gt = right + 1  # arr[gt...right] > v
    i = left + 1  # arr[lt+1...i] == v

    while i < gt:
        if data[i] < pivot:
            data[i], data[lt + 1] = data[lt + 1], data[i]
            lt += 1
            i += 1
        elif data[i] > pivot:
            data[i], data[gt - 1] = data[gt - 1], data[i]
            gt -= 1
        else:
            i += 1
    # 最后把第一个元素（基准元素）放到等于v的部分
    data[left], data[lt] = data[lt], data[left]
    
    return lt, gt


def quick_sort_9(data, left, right):
    if left >= right: return
    if right - left + 1 < 10:
        insertion_sort_quick(data)
    else:
        lt, gt = partition9(data, left, right)

        # left
        quick_sort_9(data, left, lt - 1)

        # right
        quick_sort_9(data, gt, right)




'''
优化3：优化递归操作

快排函数在函数尾部有两次递归操作，我们可以对其使用尾递归优化

优点：如果待排序的序列划分极端不平衡，递归的深度将趋近于n，而栈的大小是很有限的，每次递归调用都会耗费一定的栈空间，

函数的参数越多，每次递归耗费的空间也越多。优化后，可以缩减堆栈深度，由原来的O(n)缩减为O(logn)，将会提高性能。

使用版本8中的partition8函数
'''

def quick_sort_10(data, left, right):
    if left >= right: return
    if right - left + 1 < 10:
        insertion_sort_quick(data)
    else:
        while left < right:
            pivot = partition8(data,left,right)
            quick_sort_10(data, left, pivot-1)
            left = pivot+1

