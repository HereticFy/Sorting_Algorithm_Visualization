from tkinter import *
from tkinter import  ttk
import  random

#实例化object，建立窗口window
root = Tk()
#给窗口的可视化起名字
root.title("Sorting Algorithm Visualisation")

root.maxsize(900,900)
root.config(bg = "black")

#variables
selected_alg = StringVar()

def drawData(data):
    canvas.delete("all")

    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10

    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill = "red")
        canvas.create_text(x0+2, y0, anchor = SW, text = str(data[i]))


def Generate():
    print("Algo Selected: "+selected_alg.get())
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1

    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 10

    try:
        size = int(sizeEntry.get())
    except:
        size = 10

    if minVal <= 0 : minVal = 1
    if maxVal > 100 : maxVal = 100
    if size > 30 or size < 5 : size = 10
    if minVal > maxVal : minVal, maxVal = maxVal, minVal

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data)


#frame / base layout

# UI : User interface design 用户界面设计
#frame : 框架
#  grid有两个最为重要的参数，用来指定将组件放置到什么位置，一个是row,另一个是column。如果不指定row,会将组件放置到第一个可用的行上，如果不指定column，则使用第一列。
UI_frame = Frame(root, width = 600, height = 200, bg = 'gray')
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

#Canvas：画布，提供绘图功能(直线、椭圆、多边形、矩形) 可以包含图形或位图，用来绘制图表和图，创建图形编辑器，实现定制窗口部件。
canvas = Canvas(root, width = 600, height = 380, bg = "white")
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

#User Interface Area
#Row[0]
Label(UI_frame, text = "Algorithm: ", bg = "grey").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
algMenu = ttk.Combobox(UI_frame,textvariable = selected_alg, values = ["Bubble Sort", "Merge Sort"])
algMenu.grid(row = 0, column = 1, padx = 5, pady = 5)
algMenu.current(0)


#Row[1]
Label(UI_frame, text = "Size: ", bg = "grey").grid(row = 1, column = 0, padx = 5, pady = 5, sticky = W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

Label(UI_frame, text = "Min Value: ", bg = "grey").grid(row = 1, column = 2, padx = 5, pady = 5, sticky = W)
minEntry = Entry(UI_frame)
minEntry.grid(row = 1, column = 3, padx = 5, pady = 5, sticky = W)

Label(UI_frame, text = "Max Value: ", bg = "grey").grid(row = 1, column = 4, padx = 5, pady = 5, sticky = W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row = 1, column = 5, padx = 5, pady = 5, sticky = W)

Button(UI_frame,text = "Generate", command = Generate, bg = "white").grid(row = 0,column = 2,padx = 5, pady = 5)
#主窗口循环显示
root.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，
# 如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，
# mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。