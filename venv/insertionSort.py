import time

'''
插入排序核心：通过构建有序序列，对于未排序序列，在已排序序列中从后向前扫描(对于单向链表则只能从前往后遍历)，

找到相应位置并插入。实现上通常使用in-place排序(需用到O(1)的额外空间)

算法复杂度

1.        时间复杂度：O(n^2)

       直接插入排序耗时的操作有：比较+后移赋值。时间复杂度如下：

1)        最好情况：序列是升序排列，在这种情况下，需要进行的比较操作需（n-1）次。后移赋值操作为0次。即O(n)

2)        最坏情况：序列是降序排列，那么此时需要进行的比较共有n(n-1)/2次。后移赋值操作是比较操作的次数加上 (n-1）次。即O(n^2)

3)        渐进时间复杂度（平均时间复杂度）：O(n^2)

2.        空间复杂度：O(1)

从实现原理可知，直接插入排序是在原输入数组上进行后移赋值操作的（称“就地排序”），所需开辟的辅助空间跟输入数组规模无关，所以空间复杂度为：O(1)

 

稳定性

直接插入排序是稳定的，不会改变相同元素的相对顺序。
'''

'''
版本1：使用交换的方法
'''


def insertion_sort(data, drawData, timeTick):
    n = len(data)
    for i in range(1, n):
        temp = data[i]
        ind = i
        while ind > 0 and data[ind - 1] > temp:
            drawData(data, getColorArray(len(data), i, ind - 1))
            time.sleep(timeTick)
            data[ind] = data[ind - 1]
            ind = ind - 1
        data[ind] = temp
        drawData(data, getColorArray(len(data), i, len(data)))
        time.sleep(timeTick)


'''
版本2：使用删除再插入方法
'''


def insertion_sort_2(data, drawData, timeTick):
    n = len(data)
    for i in range(1, n):
        temp = data[i]
        ind = i
        while ind > 0 and data[ind - 1] > temp:
            drawData(data, getColorArray(len(data), i, ind - 1))
            time.sleep(timeTick)
            ind = ind - 1
        res = data.pop(i)
        data.insert(ind, res)
        drawData(data, getColorArray(len(data), i, len(data)))
        time.sleep(timeTick)


'''
版本3：插入排序的优化，在查找的时候因为前面一部分数组已经排好序了，直接用二分查找来找到插入位置

算法复杂度

1.        时间复杂度：O(n^2)

二分查找插入位置，因为不是查找相等值，而是基于比较查插入合适的位置，所以必须查到最后一个元素才知道插入位置。

二分查找最坏时间复杂度：当2^X>=n时，查询结束，所以查询的次数就为x，而x等于log2n（以2为底，n的对数）。即O(log2n)

所以，二分查找排序比较次数为：x=log2n

二分查找插入排序耗时的操作有：比较 + 后移赋值。时间复杂度如下：

1)        最好情况：查找的位置是有序区的最后一位后面一位，则无须进行后移赋值操作，其比较次数为：log2n  。即O(log2n)

2)        最坏情况：查找的位置是有序区的第一个位置，则需要的比较次数为：log2n，需要的赋值操作次数为n(n-1)/2加上 (n-1) 次。即O(n^2)

3)        渐进时间复杂度（平均时间复杂度）：O(n^2)

2.        空间复杂度：O(1)

从实现原理可知，二分查找插入排序是在原输入数组上进行后移赋值操作的（称“就地排序”），所需开辟的辅助空间跟输入数组规模无关，所以空间复杂度为：O(1)

稳定性

二分查找排序是稳定的，不会改变相同元素的相对顺序。
'''


def insertion_sort_quick(data):
    if data == None or not data: return data
    n = len(data)
    for i in range(1, n):
        temp = data[i]
        beg = 0
        end = i - 1
        while beg <= end:
            mid = beg + (end - beg) // 2
            if temp > data[mid]:
                beg = mid + 1
            else:
                end = mid - 1
        res = data.pop(i)
        data.insert(beg, res)


'''
希尔排序

概念及实现

思想：分治策略

希尔排序是一种分组直接插入排序方法，其原理是：先将整个序列分割成若干小的子序列，再分别对子序列进行直接插入排序，

使得原来序列成为基本有序。这样通过对较小的序列进行插入排序，然后对基本有序的数列进行插入排序，能够提高插入排序算法的效率。

具体如下（实现为升序）：

1.先取一个小于n的整数d1作为第一个增量，将所有距离为d1的倍数的记录放在同一个组中，把无序数组分割为若干个子序列。

2.在各子序列内进行直接插入排序。

3.然后取第二个增量d2<d1，重复步骤1~2，直至所取的增量dt=1(dt<dt-l<…<d2<d1)，即所有记录放在同一组中进行直接插入排序为止。

算法复杂度

1.时间复杂度: O(nlog2n)

希尔排序耗时的操作有：比较 + 后移赋值。时间复杂度如下：

1)最好情况：序列是升序排列，在这种情况下，需要进行的比较操作需（n-1）次。后移赋值操作为0次。即O(n)

2)最坏情况：O(nlog2n)。

3)渐进时间复杂度（平均时间复杂度）：O(nlog2n)

       增量选取：希尔排序的时间复杂度与增量的选取有关，但是现今仍然没有人能找出希尔排序的精确下界。一般的选择原则是：取上一个增量的一半作为此次序列的划分增量。首次选择序列长度的一半为增量。（因此也叫缩小增量排序）

       平均时间复杂度：O(nlog2n)，希尔排序在最坏的情况下和平均情况下执行效率相差不是很多，与此同时快速排序（O(log2n)）在最坏的情况下执行的效率会非常差。专家们提倡，几乎任何排序工作在开始时都可以用希尔排序，若在实际使用中证明它不够快，再改成快速排序这样更高级的排序算法.  

 

2.空间复杂度：O(1)

从实现原理可知，希尔排序是在原输入数组上进行后移赋值操作的（称“就地排序”），所需开辟的辅助空间跟输入数组规模无关，所以空间复杂度为：O(1)

 

稳定性

希尔排序是不稳定的。因为在进行分组时，相同元素可能分到不同组中，改变相同元素的相对顺序。

 

优化改进

根据实际运行情况，我们也可以将希尔排序中查找插入位置部分的代码替换为二分查找方式。
'''


def shell_sort(data, drawData, timeTick):
    n = len(data)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                drawData(data, getColorArrayShell(len(data), i, j - gap, gap))
                time.sleep(timeTick)
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap = gap // 2


def getColorArray(dataLen, ind, comp):
    colorArr = []
    for i in range(dataLen):
        if i == ind:
            colorArr.append("pink")
        elif i == comp:
            colorArr.append("yellow")
        elif i < ind:
            colorArr.append('blue')
        else:
            colorArr.append("red")
    return colorArr


def getColorArrayShell(dataLen, ind, comp, gap):
    colorArr = ["red" for i in range(dataLen)]
    temp = ind
    while temp < dataLen:
        colorArr[temp] = "purple"
        temp += gap
    temp = ind
    while temp >= 0:
        colorArr[temp] = "purple"
        temp -= gap
    for i in range(dataLen):
        if i == ind:
            colorArr[i] = "pink"
        elif i == comp:
            colorArr[i] = "yellow"
    return colorArr
