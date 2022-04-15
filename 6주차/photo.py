from tkinter import *

#함수 선언
def myFunc() :
    if var.get() == 1 :
        labelImage.configure(image = photo1)  # 그림 설정한 공간에 이미지를 대체
    elif var.get() == 2 :
        labelImage.configure(image = photo2)
    else :
        labelImage.configure(image=photo3)

# 전역 변수 선언 부분
var, labelImage = 0, None


#메인 코드 부분
if __name__ == "__main__" :
    window = Tk()
    window.geometry("400x400")
    window.title("애완동물 선택하기")
    labelText = Label(window, text = "좋아하는 동물 투표",fg = "blue", font = ("궁서체", 20))  #글씨 쓰기

    var = IntVar()
    rb1 = Radiobutton(window, text = "강아지", variable = var, value = 1)
    rb2 = Radiobutton(window, text = "고양이", variable = var, value = 2)
    rb3 = Radiobutton(window, text = "토끼", variable = var, value = 3)
    buttonOk = Button(window, text = "사진 보기", command = myFunc)

    photo1 = PhotoImage(file = "C:/Users/송빈원/Desktop/오픈소스기초[알고리즘]/Opensource/6주차/image/dog.gif")
    photo2 = PhotoImage(file = "C:/Users/송빈원/Desktop/오픈소스기초[알고리즘]/Opensource/6주차/image/cat.gif")
    photo3 = PhotoImage(file = "C:/Users/송빈원/Desktop/오픈소스기초[알고리즘]/Opensource/6주차/image/rabbit.gif")  #절대주소로 설정

    labelImage = Label(window, width = 200, height = 200, bg = "yellow",image = None)   #그림을 표시할 공간설정

    labelText.pack(padx = 5, pady = 5)
    rb1.pack(padx = 5, pady = 5)
    rb2.pack(padx=5, pady=5)
    rb3.pack(padx=5, pady=5)
    buttonOk.pack(padx=5, pady=5)
    labelImage.pack(padx=5, pady=5)

    window.mainloop()