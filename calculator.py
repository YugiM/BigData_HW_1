from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry('328x300')
window.resizable(0,0)

frame1 = Frame(window)
frame1.pack(side = TOP, fill = X)

frame2 = Frame(window)
frame2.pack(side = BOTTOM, fill = X)

equation = StringVar()
expression = ''
txt = Entry(frame1, width = 50, textvariable = equation, relief=RIDGE, justify = RIGHT, bd = 9, bg = "gray55", font = ('arial', 20, 'bold'))
txt.pack(ipady = 16)

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def clicked_btnac():
    global expression
    expression = ''
    equation.set("")

def equal():
    global expression
    res = str(eval(expression))
    equation.set(res)
    expression = ''

btnl = Button(frame2, text='(', width = 10, height = 2, command = lambda: press("("), highlightthickness = 2, bg = 'gray67')
btnl.grid(column = 1, row = 4)
btnr = Button(frame2, text=')', width = 10, height = 2, command = lambda: press(")"), highlightthickness = 2, bg = 'gray67')
btnr.grid(column = 2, row = 4)
btnac = Button(frame2, text='AC', width = 10, height = 2, command = clicked_btnac, highlightthickness = 2, bg = 'tan1', fg = 'LightYellow2')
btnac.grid(column = 3, row = 4)
btno = Button(frame2, text='/', width = 10, height = 2, command = lambda: press("/"), highlightthickness = 2, bg = 'tan1', fg = 'LightYellow2')
btno.grid(column = 4, row = 4)
btn7 = Button(frame2, text='7', width = 10, height = 2, command = lambda: press(7), highlightthickness = 2, bg = 'gray67')
btn7.grid(column = 1, row = 5)
btn8 = Button(frame2, text='8', width = 10, height = 2, command = lambda: press(8), highlightthickness = 2, bg = 'gray67')
btn8.grid(column = 2, row = 5)
btn9 = Button(frame2, text='9', width = 10, height = 2, command = lambda: press(9), highlightthickness = 2, bg = 'gray67')
btn9.grid(column = 3, row = 5)
btnt = Button(frame2, text='x', width = 10, height = 2, command = lambda: press("*"), highlightthickness = 2, bg = 'tan1', fg = 'LightYellow2')
btnt.grid(column = 4, row = 5)
btn4 = Button(frame2, text='4', width = 10, height = 2, command = lambda: press(4), highlightthickness = 2, bg = 'gray67')
btn4.grid(column = 1, row = 6)
btn5 = Button(frame2, text='5', width = 10, height = 2, command = lambda: press(5), highlightthickness = 2, bg = 'gray67')
btn5.grid(column = 2, row = 6)
btn6 = Button(frame2, text='6', width = 10, height = 2, command = lambda: press(6), highlightthickness = 2, bg = 'gray67')
btn6.grid(column = 3, row = 6)
btnd = Button(frame2, text='-', width = 10, height = 2, command = lambda: press("-"), highlightthickness = 2, bg = 'tan1', fg = 'LightYellow2')
btnd.grid(column = 4, row = 6)
btn1 = Button(frame2, text='1', width = 10, height = 2, command = lambda: press(1), highlightthickness = 2, bg = 'gray67')
btn1.grid(column = 1, row = 7)
btn2 = Button(frame2, text='2', width = 10, height = 2, command = lambda: press(2), highlightthickness = 2, bg = 'gray67')
btn2.grid(column = 2, row = 7)
btn3 = Button(frame2, text='3', width = 10, height = 2, command = lambda: press(3), highlightthickness = 2, bg = 'gray67')
btn3.grid(column = 3, row = 7)
btnp = Button(frame2, text='+', width = 10, height = 2, command = lambda: press("+"), highlightthickness = 2, bg = 'tan1', fg = 'LightYellow2')
btnp.grid(column = 4, row = 7)
btn0 = Button(frame2, text='0', width = 10, height = 2, command = lambda: press(0), highlightthickness = 2, bg = 'gray67')
btn0.grid(column = 1, row = 8)
btnn = Button(frame2, text='.', width = 10, height = 2, command = lambda: press("."), highlightthickness = 2, bg = 'gray67')
btnn.grid(column = 2, row = 8)
btne = Button(frame2, text='=', width = 22, height = 2, highlightthickness = 2, command = equal, bg = 'IndianRed1', fg = 'LightYellow2')
btne.grid(column = 3, row = 8, columnspan = 2)

window.mainloop()   
