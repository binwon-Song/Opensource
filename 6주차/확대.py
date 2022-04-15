from math import fabs
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *


value=1
value2=1
def func_open():
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"),
                ("모든 파일", "*.*")))
    photo = PhotoImage(file = filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit():
    window.quit()
    window.destroy() 

def func_zoom():
    global value
    value+=1
    print(value)
    photo = PhotoImage(file = filename)
    photo = photo.zoom(value,value)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_unzoom():
    global value2
    value2+=1
    print(value2)
    photo = PhotoImage(file = filename)
    photo = photo.subsample(value2,value2)
    pLabel.configure(image = photo)
    pLabel.image = photo
    value=-value
def KeyClick(e):
    global key
    key=e.keysym
    if key=='Up':    #KEY값이 위쪽아면
        func_zoom()
    elif key=='Down':   #KEY값이 아래쪽이면
        func_unzoom()
window = Tk()
window.geometry("400x400")
window.title("확대 축소")

photo = PhotoImage()
pLabel = Label(window,image = photo)
pLabel.pack(expand = 1, anchor = CENTER)

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일',menu = fileMenu)
fileMenu.add_command(label = '파일 열기', command = func_open)
fileMenu.add_separator()
fileMenu.add_command(label = '프로그램 종료', command = func_exit)
window.bind("<Key>",KeyClick)  #KEY값 입력받기
window.mainloop()