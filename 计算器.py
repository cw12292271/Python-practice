# 第一步： 画出图形界面上半部
from tkinter import *

root = Tk()
# 定义面板的大小
root.geometry('250x380')
root.title("太一计算")

# 定义面板
# bg代表背景颜色（background）， #dddddd是十六进制表示颜色的一个串
frame_show = Frame(width=250, height=150, bg='#dddddd')
frame_show.pack()

# 定义顶部区域

sv = StringVar()
sv.set('0')
# result = StringVar()
# result.set('')
# anchor:定义控件的锚点，e代表右边
# font代表字体
show_label = Label(frame_show, textvariable=sv, \
                   bg='white', width=12, height=2, \
                   font=("黑体", 20, 'bold'), \
                   justify=LEFT, anchor='w')
show_label.pack(padx=10, pady=10)

# 第二步： 画出图形界面下半部
def delete():
    if len(sv.get()) == 1:
        sv.set('0')
    else:
        sv.set(str(sv.get()[:-1]))


def clear():
    sv.set('0')


# 按键区域
frame_bord = Frame(width=600, height=500, bg='#cccccc')

b_del = Button(frame_bord, text="DEL", width=10, height=1, \
               command=delete).grid(row=0, column=0, columnspan=2, rowspan=1, sticky=W + E)

button_clear = Button(frame_bord, text='C', width=10, height=1, \
                      command=clear).grid(row=0, column=2, columnspan=2, rowspan=1, sticky=W + E)

# 数字按钮
b_7 = Button(frame_bord, text='7', width=5, height=2, \
             command=lambda: change("7")).grid(row=1, column=0)

b_8 = Button(frame_bord, text='8', width=5, height=2, \
             command=lambda: change("8")).grid(row=1, column=1)

b_9 = Button(frame_bord, text='9', width=5, height=2, \
             command=lambda: change("9")).grid(row=1, column=2)

b_4 = Button(frame_bord, text='4', width=5, height=2, \
             command=lambda: change("4")).grid(row=2, column=0)

b_5 = Button(frame_bord, text='5', width=5, height=2, \
             command=lambda: change("5")).grid(row=2, column=1)

b_6 = Button(frame_bord, text='6', width=5, height=2, \
             command=lambda: change("6")).grid(row=2, column=2)

b_3 = Button(frame_bord, text='3', width=5, height=2, \
             command=lambda: change("3")).grid(row=3, column=0)

b_2 = Button(frame_bord, text='2', width=5, height=2, \
             command=lambda: change("2")).grid(row=3, column=1)

b_1 = Button(frame_bord, text='1', width=5, height=2, \
             command=lambda: change("1")).grid(row=3, column=2)

b_0 = Button(frame_bord, text='0', width=5, height=2, \
             command=lambda: change("0")).grid(row=4, column=1)

# 运算符
b_add = Button(frame_bord, text='+', width=5, height=2, \
               command=lambda: change("+")).grid(row=1, column=3)
b_sub = Button(frame_bord, text='-', width=5, height=2, \
               command=lambda: change("-")).grid(row=2, column=3)
b_mul = Button(frame_bord, text='×', width=5, height=2, \
               command=lambda: change("*")).grid(row=3, column=3)
b_div = Button(frame_bord, text='/', width=5, height=2, \
               command=lambda: change("/")).grid(row=4, column=0)
b_point = Button(frame_bord, text='.', width=5, height=2, \
                 command=lambda: change(".")).grid(row=4, column=2)

b_equ = Button(frame_bord, text='=', width=5, height=2, \
               command=lambda: calculate()).grid(row=4, column=3)

'''
考虑以下集中情况：
1. 按下数字
2. 按下操作符号
3，只考虑两个操作数操作，比考虑复杂情况

'''

def change(buttonString):
    '''
    按下一个数字需要考虑两种情况：
    1. 数字属于第一个操作数
    2. 数字属于第二个操作数
    3. 判断是否属于第一个操作数，可以通过operator判断
    '''
    content = sv.get()
    if content == "0":
        content = ""
    # if "." in content and buttonString == ".":
    #     buttonString = ""
    content = content + buttonString
    sv.set(content)


def calculate():
    result = '%.4f' %(eval(sv.get()))

    sv.set(sv.get() + '=\n' + str(result))




frame_bord.pack(padx=10, pady=10)

root.mainloop()