from cmath import tan
import turtle,random
from tkinter.simpledialog import askstring
import math
inStr=''
swidth,sheight=500,500
tx=200;ty=0;txtsize=20
turtle.title('거북이 나선형')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)   #창 설정
turtle.penup()
turtle.goto(tx,ty)   #
inStr=askstring('문자열 입력','거북이가 쓸 문자열 입력')   #문자열 입력 창

l=len(inStr)
angle=(360*2)/l

###### 2019038036   송빈원   ######
dist=200
ddist=200
Dist=200
for ch in inStr:
    dist-=ddist/l
    Dist-=angle
    radian=(3.14*Dist)/180  #라디안 값
    tx=dist*math.cos(radian)
    ty=dist*math.sin(radian)
    r=random.random();g=random.random();b=random.random()
    
    turtle.goto(tx,ty)
    
    turtle.pencolor(r,g,b)
    turtle.write(ch,font=('맑은고딕',txtsize,'bold'))   #글쓰기
    
turtle.done()
