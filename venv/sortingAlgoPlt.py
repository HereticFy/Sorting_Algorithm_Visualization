from matplotlib import pyplot as plt
import random

LIST_SIZE = 40
PAUSE_TIME = 4 / LIST_SIZE


# 冒泡算法
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            plt.cla()  # 清除内容
            plt.bar(range(len(nums)), nums, align='center')
            plt.bar(j, nums[j], color="r", align="center")
            plt.bar(j + 1, nums[j + 1], color="r", align="center")
            plt.pause(PAUSE_TIME)
    plt.show()


# 插入排序
def insert_sort(nums):
    for i in range(1, len(nums)):
        pos = 0
        for j in range(i - 1, -1, -1):
            if nums[i] > nums[j]:
                pos = j + 1
                break
        temp = nums[i]
        for x in range(i, pos - 1, -1):
            nums[x] = nums[x - 1]
            nums[pos] = temp
            plt.cla()  # 清除内容
            plt.bar(range(len(nums)), nums, align='center')
            plt.bar(i, nums[i], color="r", align="center")
            plt.bar(x, nums[x], color="g", align="center")
            plt.bar(pos, nums[pos], color="r", align="center")
            plt.pause(PAUSE_TIME)
    plt.show()


# 选择排序
def selection_sort(nums):
    for i in range(0, len(nums)):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
            plt.cla()  # 清除内容
            plt.bar(range(len(nums)), nums, align='center')
            plt.bar(i, nums[i], color="r", align="center")
            plt.bar(j, nums[j], color="r", align="center")
            plt.pause(PAUSE_TIME)
        nums[i], nums[min] = nums[min], nums[i]
    plt.show()


# 希尔排序
def shell_sort(nums):
    step = len(nums)
    while True:
        step = int(step / 3 + 1)
        for n in range(step):
            for i in range(n + step, len(nums), step):
                pos = n
                for j in range(i - step, -1, -step):
                    if nums[i] > nums[j]:
                        pos = j + step
                        break
                temp = nums[i]
                for x in range(i, pos - step, -step):
                    plt.cla()  # 清除内容
                    nums[x] = nums[x - step]
                    plt.bar(range(len(nums)), nums, align='center')
                    plt.bar(pos, nums[pos], color="r", align="center")
                    plt.bar(x, nums[x], color="r", align="center")
                    plt.pause(PAUSE_TIME)
                nums[pos] = temp
        if step <= 1:
            break
    plt.show()


nums = []
for i in range(LIST_SIZE):
    nums.append(random.randint(0, 1000))

insert_sort(nums)

print(nums)