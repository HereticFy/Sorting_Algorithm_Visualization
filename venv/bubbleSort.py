import time

'''
冒泡排序算法的运作如下：

1、比较相邻的元素。如果第一个比第二个大（小），就交换他们两个。

2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大（小）的数。

3、针对所有的元素重复以上的步骤，除了最后已经选出的元素（有序）。

4、持续每次对越来越少的元素（无序元素）重复上面的步骤，直到没有任何一对数字需要比较，则序列最终有序。


（1）时间复杂度

在设置标志变量之后：

当原始序列“正序”排列时，冒泡排序总的比较次数为n-1，移动次数为0，也就是说冒泡排序在最好情况下的时间复杂度为O(n)；

当原始序列“逆序”排序时，冒泡排序总的比较次数为n(n-1)/2，移动次数为3n(n-1)/2次，所以冒泡排序在最坏情况下的时间复杂度为O(n^2)；

当原始序列杂乱无序时，冒泡排序的平均时间复杂度为O(n^2)。



（2）空间复杂度

冒泡排序排序过程中需要一个临时变量进行两两交换，所需要的额外空间为1，因此空间复杂度为O(1)。



（3）稳定性

冒泡排序在排序过程中，元素两两交换时，相同元素的前后顺序并没有改变，所以冒泡排序是一种稳定排序算法。

'''

def bubble_sort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j+1]:
                drawData(data, ["blue" if x == j or x == j + 1 else "red" for x in range(len(data))])
                time.sleep(timeTick)
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ["green" if x == j or x == j+1 else "red" for x in range(len(data))])
                time.sleep(timeTick)

    drawData(data, ["green" for x in range(len(data))])

'''
加入change改良的原理是在发现没有发生两两交换的时候则说明数组已经排好序了，不用继续遍历了
'''
def bubble_sort_change(data, drawData, timeTick):
    for _ in range(len(data) - 1):
        swap = False
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
                drawData(data, ["green" if x == j or x == j+1 else "red" for x in range(len(data))])
                time.sleep(timeTick)
        if swap == False: break

    drawData(data, ["green" for x in range(len(data))])

'''
在加入change的基础上再次改良：
加入border参数，让我们知道最后一次发生交换的位置在哪，这样的话，下次开始遍历只用到这个border就行了，因为border后面的数都排好序了，不用交换了
'''
def bubble_sort_border(data, drawData, timeTick):
    border = len(data) - 1
    for _ in range(len(data) - 1):
        swap = False
        for j in range(0, border):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swap = True
                drawData(data, ["green" if x == j or x == j+1 else "red" for x in range(len(data))])
                time.sleep(timeTick)
                last_index_change = j
        if swap == False: break

        border = last_index_change

    drawData(data, ["green" for x in range(len(data))])




'''
拓展，冒泡排序的变形： 鸡尾酒排序

鸡尾酒排序又叫定向冒泡排序，搅拌排序、来回排序等，是冒泡排序的一种变形。此算法与冒泡排序的不同处在于排序时是以双向在序列中进行排序。

鸡尾酒排序在于排序过程是先从低到高，然后从高到低；而冒泡排序则仅从低到高去比较序列里的每个元素。它可以得到比冒泡排序稍微好一点的效能，

原因是冒泡排序只从一个方向进行比对（由低到高），每次循环只移动一个项目。
'''
def cocktail_sort(data, drawData, timeTick):
    left, right = 0, len(data)-1
    while(left < right):
        for i in range(left,right):
            if data[i] > data[i+1]: data[i], data[i+1] = data[i+1], data[i]
            drawData(data, ["green" if x == i or x == i + 1 else "red" for x in range(len(data))])
        right -= 1
        for k in range(right, left, -1):
            if data[k-1] > data[k]: data[k-1], data[k] = data[k], data[k-1]
            drawData(data, ["green" if x == k or x == k + 1 else "red" for x in range(len(data))])
        left += 1

    drawData(data, ["green" for x in range(len(data))])

a = [[0] * 2] * 2

a[0][0] = 1 

print(a)