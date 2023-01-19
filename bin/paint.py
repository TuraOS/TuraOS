from tkinter import *
from tkinter import colorchooser
import subprocess
from subprocess import call

root = Tk()
root.title("TuraOS Paint")
root.geometry("600x580+270+0")

brush_color = 'black'
brush_type = StringVar()
brush_type.set("round")

def paint(e):
    x1,y1 = e.x-1,e.y-1
    x2,y2 = e.x, e.y
    brush = brush_type.get()
    my_canvas.create_line(x1,y1,x2,y2,fill = brush_color, width = 10, capstyle=brush)


def change_brush_color():
    global brush_color
    brush_color = colorchooser.askcolor(color=brush_color)[1]

def erase():
    global brush_color
    brush_color = 'white'

def clear_screen():
    my_canvas.delete(ALL)



my_canvas = Canvas(root, width=500, height=480, bg='white')
my_canvas.pack(side="bottom", fill="both")
my_canvas.bind('<B1-Motion>',paint)

tools = LabelFrame(root, text="Paint Tools", font=('Helvetica', 12, 'bold'))
tools.pack(side="top", fill="both", expand="yes")

brush_color_button = Button(tools, text="Brush Color",font=('Sans', 10, 'bold'),command=change_brush_color)
brush_color_button.place(x=30, y=10)

brush_type_label = Label(tools, text="Brush Type", relief="raised", width=11 , font=('Sans', 10, 'bold'))
brush_type_menu = OptionMenu(tools, brush_type, "round", "butt", "projecting")
brush_type_menu.config(font=('Sans', 10, 'bold'))
brush_type_menu.place(x=180, y=35)

erase = Button(tools, text="Eraser",font=('Sans', 10, 'bold'), command=erase)
erase.place(x=340, y=10)

clear_screen = Button(tools, text='Clear Screen', font=('Sans', 10, 'bold'), command=clear_screen)
clear_screen.place(x=460, y=10)


root.mainloop()


def open_py_file():
    call(["python", "C:\\Users\\Admin\\Desktop\\TuraOS\\term\\terminal.py"])

open_py_file()