import time
'''
计数排序
如果在面试中有面试官要求你写一个O(n)时间复杂度的排序算法，你千万不要立刻说：这不可能！

虽然前面基于比较的排序的下限是O(nlogn)。但是确实也有线性时间复杂度的排序，只不过有前提条件，就是待排序的数要满足一定的范围的整数，而且计数排序需要比较多的辅助空间。其基本思想是，用待排序的数作为计数数组的下标，统计每个数字的个数。然后依次输出即可得到有序序列。

计数排序原理：

找到给定序列的最小值与最大值

创建一个长度为最大值-最小值+1的数组，初始化都为0

然后遍历原序列，并为数组中索引为当前值－最小值的值＋１

此时数组中已经记录好每个值的数量，自然也就是有序的了

复杂度：O(N)
'''

def count_sort(data, drawData, timeTick):
    """计数排序"""
    # 找到最大最小值
    min_num = min(data)
    max_num = max(data)
    # 计数列表
    count_list = [0]*(max_num-min_num+1)
    # 计数
    for i in data:
        count_list[i-min_num] += 1
        drawData(count_list, ["blue" if j == i else "red" for j in range(len(count_list))])
        time.sleep(timeTick)
    data.clear()
    # 填回
    for ind,i in enumerate(count_list):
        while i != 0:
            data.append(ind+min_num)
            drawData(data, ["blue" if j == len(data) - 1 else "red" for j in range(len(data))])
            time.sleep(timeTick)
            i -= 1


