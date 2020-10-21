import time
import random

'''
堆排序

堆排序是利用堆这种数据结构而设计的一种排序算法，堆排序是一种选择排序，

它的最坏，最好，平均时间复杂度均为O(nlogn)，它也是不稳定排序。首先简单了解下堆结构。

堆

堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；

或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆

堆排序的基本思想是：将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。

将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。

如此反复执行，便能得到一个有序序列了

总结：

构建堆：

首先遍历列表，选定一个节点（元素）i， 2*i+1是它的左节点 2*i+2则是它的右节点 如果这两个数没有超出列表边界

然后比较三者的大小关系，如果没有问题，就跳过。 

如果有问题，那么交换三者中最大（小）节点和父节点的位置，然后对于这个原始最大（小）节点进行递归操作检查

因为交换位置后可能会破坏堆的结构，所以要检查一下！ 

堆排序：

把堆整理好了后，我们要把根节点和最后末尾的节点的值互换，然后除去末尾节点

这样最大（小）的元素就被选出来了！ 但是此时堆的结构就被破坏了！

所以这个时候我们就需要维护一下我们的堆，记住：这个时候堆的那个尾节点是被去除掉了的

等堆维护好了，根节点又是这个堆里最大（小）的值了，我们就重复上述操作，直到堆里没有元素位置，列表就排好序了！
'''

'''
构建一个大顶堆
'''


def max_heapify(data, length, root):  # 在堆中做结构调整使得父节点的值大于子节点

    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < length and data[larger] < data[left]:
        larger = left
    if right < length and data[larger] < data[right]:
        larger = right
    if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        data[larger], data[root] = data[root], data[larger]
        max_heapify(data, length, larger)


def build_max_heap(data):  # 构造一个堆，将堆中所有数据重新排序
    length = len(data)  # 将堆的长度当独拿出来方便
    for i in range((length - 2) // 2, -1, -1):  # 从后往前出数
        max_heapify(data, length, i)


def heap_sort(data, drawData, timeTick):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    build_max_heap(data)
    for i in range(len(data) - 1, -1, -1):
        drawData(data, getColorArray(len(data), i))
        time.sleep(timeTick)
        data[0], data[i] = data[i], data[0]
        max_heapify(data, i, 0)
    return data


'''def max_heap_sort(data, drawData, timeTick):
    build_max_heap(data)

    for j in range(len(data) - 1, -1, -1):
        #drawData(data, getColorArray(len(data), j))
        #time.sleep(timeTick)
        data[0], data[j] = data[j], data[0]
        adjust_max_heap(data, 0, j - 1)
    #drawData(data, getColorArray(len(data), j))'''


def getColorArray(dataLen, index):
    colors = ["red" for i in range(dataLen)]
    for i in range(dataLen):
        if i == index:
            colors[i] = "blue"
        if i > index:
            colors[i] = "green"
    return colors


'''
构建一个小堆顶
'''


def min_heapify(data, length, root):  # 在堆中做结构调整使得父节点的值大于子节点

    left = 2 * root + 1
    right = left + 1
    smaller = root
    
    if left < length and data[smaller] > data[left]:
        smaller = left
    if right < length and data[smaller] > data[right]:
        smaller = right
    if smaller != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
        data[smaller], data[root] = data[root], data[smaller]
        max_heapify(data, length, smaller)


def build_min_heap(data):  # 构造一个堆，将堆中所有数据重新排序
    length = len(data)  # 将堆的长度当独拿出来方便
    for i in range((length - 2) // 2, -1, -1):  # 从后往前出数
        min_heapify(data, length, i)




'''
解决top-k问题

利用堆来进行实现

        *我们首先建立一个K大小的堆，

        *接着，我们是要找最大的前K个数，我们应该建大堆还是小堆呢，可能很多读者会不假思索的说建大堆，

        但是我们来仔细的考虑下，如果建大堆的话，堆顶的元素就是最大的，那么后面的元素就进不来了，只会找到一个最大的元素，所以我们要建小堆。

        *我们建好堆后，每次将来的一个元素和堆顶的元素进行比较，如果大于堆顶的元素的话，

        那么我们就将此元素直接赋给堆顶的元素。然后进行向下调整。
'''


def heap_adjust(data, i, size):
    left = 2 * i + 1
    right = 2 * i + 2
    min_index = i
    if (left < size and data[min_index] > data[left]):
        min_index = left
    if (right < size and data[min_index] > data[right]):
        min_index = right
    if (min_index != i):
        temp = data[min_index]
        data[min_index] = data[i]
        data[i] = temp
        heap_adjust(data, min_index, size)
    return data


def build_heap(data, size):
    for i in range(int(size / 2), -1, -1):
        heap_adjust(data, i, size)
    return data


