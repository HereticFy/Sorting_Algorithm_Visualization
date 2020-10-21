'''
还有计数排序， 堆排序， 桶排序， 基数排序没有添加。。。

'''

from tkinter import *
from tkinter import ttk
import random
from bubbleSort import *
from quickSort import *
import threading
from mergeSort import *
from insertionSort import *
from selectionSort import *
from heapsort import *
from countSort import *

# 实例化object，建立窗口window
root = Tk()
# 给窗口的可视化起名字
root.title("Sorting Algorithm Visualisation")

root.maxsize(900, 900)
root.config(bg="black")

# variables
selected_alg = StringVar()
data = []


def thread_it(func, *args):  # 卡死主要是因为这里给他改成多线程处理就可以啦！！！
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


def drawData(data, colorArray):
    canvas.delete("all")

    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10

    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        # top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def Generate():
    global data
    print("Algo Selected: " + selected_alg.get())

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data, ["red" for x in range(len(data))])


def StartAlgorithm():
    global data

    if not data: return

    if (algMenu.get() == "Quick Sort"):
        quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())

    elif algMenu.get() == "Bubble Sort":
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() == "Merge Sort":
        merge_sort(data, drawData, speedScale.get())

    elif algMenu.get() == "Insertion Sort":
        insertion_sort(data, drawData, speedScale.get())

    elif algMenu.get() == "Insertion Sort Ver2":
        insertion_sort_2(data, drawData, speedScale.get())

    elif algMenu.get() == "Selection Sort":
        selection_sort(data, drawData, speedScale.get())

    elif algMenu.get() == "Shell Sort":
        shell_sort(data, drawData, speedScale.get())

    elif algMenu.get() == "Heap Sort":
        heap_sort(data, drawData, speedScale.get())

    elif algMenu.get() == "Count Sort":
        count_sort(data, drawData, speedScale.get())

    drawData(data, ["green" for x in range(len(data))])


# frame / base layout

# UI : User interface design 用户界面设计
# frame : 框架
#  grid有两个最为重要的参数，用来指定将组件放置到什么位置，一个是row,另一个是column。如果不指定row,会将组件放置到第一个可用的行上，如果不指定column，则使用第一列。
UI_frame = Frame(root, width=600, height=200, bg='gray')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# Canvas：画布，提供绘图功能(直线、椭圆、多边形、矩形) 可以包含图形或位图，用来绘制图表和图，创建图形编辑器，实现定制窗口部件。
canvas = Canvas(root, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface Area
# Row[0]
'''
签控件（Label）指定的窗口中显示的文本和图像。 
部分参数介绍：
anchor
文本或图像在背景内容区的位置，默认为 center，可选值为（n,s,w,e,ne,nw,sw,se,center）eswn 是东南西北英文的首字母，表示：上北下南左西右东

bg
标签背景颜色

bd
标签的大小，默认为 2 个像素

padx
x 轴间距，以像素计，默认 1。


pady
y 轴间距，以像素计，默认 1。


text
设置文本，可以包含换行符(\n)。

'''
Label(UI_frame, text="Algorithm: ", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
# Tkinter 下拉列表-combobox 是用户可用来选择的下拉列表。它是 Entry 和 drop-down 控件的组合。
# The advantage to using a StringVar comes when you want to either
# a) have two widgets share the same variable so that one is updated when the other is changed
# b) attach one or more traces to the StringVar
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg,
                       values=["Bubble Sort", "Merge Sort", "Quick Sort", "Insertion Sort"
                           , "Insertion Sort Ver2", "Selection Sort", "Shell Sort", "Heap Sort",
                               "Count Sort"])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

'''
Scale控件允许用户通过移动滑动条来选择数值。你可以设置最小值和最大值，滚动的滑条取值在最大值和最小值之间。
digits
如果用于控制比例数据的控制变量是字符串类型，则此选项用于指定将数字比例转换为字符串时的位数。
resolution
设置为对刻度值进行的最小变化。
https://www.py.cn/manual/python-tkinter-scale.html
'''
speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL,
                   label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)

'''
按钮组件用于在 Python 应用程序中添加按钮，按钮上可以放上文本或图像，按钮可用于监听用户行为，能够与一个 Python 函数关联，当按钮被按下时，自动调用该函数。
https://www.runoob.com/python/python-tk-button.html
'''
Button(UI_frame, text="Start", command=lambda: thread_it(StartAlgorithm), bg="red").grid(row=0, column=3, padx=5,
                                                                                         pady=5)

# Row[1]
'''
Entry 文本框用来让用户输入一行文本字符串。
https://www.runoob.com/python/python-tkinter-entry.html
'''
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5, sticky=W)

Button(UI_frame, text="Generate", command=Generate, bg="white").grid(row=1, column=3, padx=5, pady=5)

# 主窗口循环显示
root.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，
# 如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，
# mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
