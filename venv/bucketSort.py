'''
桶排序介绍
桶排序(Bucket sort)是一种基于计数的排序算法，工作的原理是将数据分到有限数量的桶子里，

然后每个桶再分别排序（有可能再使用别的排序算法或是以递回方式继续使用桶排序进行排序）。

当要被排序的数据内的数值是均匀分配的时候，桶排序时间复杂度为Θ(n)。桶排序不同于快速排序，并不是比较排序，

不受到时间复杂度 O(nlogn) 下限的影响。

桶排序按下面4步进行：

1. 设置固定数量的空桶。

2. 把数据放到对应的桶中。

3. 对每个不为空的桶中数据进行排序。

4. 拼接从不为空的桶中数据，得到结果。

桶排序，主要适用于小范围整数数据，且独立均匀分布，可以计算的数据量很大，而且符合线性期望时间。

1,桶排序是稳定的

2,桶排序是常见排序里最快的一种,比快排还要快…大多数情况下

3,桶排序非常快,但是同时也非常耗空间,基本上是最耗空间的一种排序算法
'''


def bucket_sort(arr):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)
    # 桶的大小
    bucket_range = (max_num-min_num) / len(arr)
    # 桶数组
    count_list = [ [] for i in range(len(arr) + 1)]
    # 向桶数组填数
    for i in arr:
        count_list[int((i-min_num)//bucket_range)].append(i)
    arr.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            arr.append(j)
