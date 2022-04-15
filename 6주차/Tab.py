from tkinter import *
import tkinter.ttk


window=Tk()
notebook=tkinter.ttk.Notebook(window, width=800, height=500)
notebook.pack()
photo1 = PhotoImage(file = "C:/Users/송빈원/Desktop/오픈소스기초[알고리즘]/Opensource/6주차/image/dog.gif")
photo2 = PhotoImage(file = "C:/Users/송빈원/Desktop/오픈소스기초[알고리즘]/Opensource/6주차/image/cat.gif")
tab1=tkinter.Frame(window)
notebook.add(tab1, text="강아지")   #탭 1개 설정
tab2=tkinter.Frame(window)
notebook.add(tab2, text="고양이")  #탭 2 설정
####### 2019038036   송빈원   ######
label1=tkinter.Label(tab1, image=photo1)  #탭 1의 이미지 설정

label1.pack()

label2=tkinter.Label(tab2, image=photo2)
label2.pack()
window.mainloop()