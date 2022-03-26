import turtle 
import random 


playerTurtles = [] 
swidth, sheight = 500, 500 ## 메인 함수 부분 ## 

turtle.setup(width = swidth + 50, height = sheight + 50) 
turtle.screensize(swidth, sheight) 

for i in range(0, 5) : 
    myTurtle = turtle.Turtle('turtle') 
    tX = random.randrange(-swidth / 2, swidth / 2) 
    tY = random.randrange(-sheight / 2, sheight / 2) 
    r = random.random(); g = random.random(); b = random.random()
    tSize = random.randrange(1, 50)/10 
    playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])  
    
sortedT = sorted(playerTurtles, key=lambda x : x[3])   # playesTurtles 의 3번째 인덱스값(사이즈)을 기준으로 정렬
    ########## 2019038036_송빈원   ####
for index, tList in enumerate(sortedT) : # 인덱스와 값을 받음
    myTurtle = tList[0]
    myTurtle.color((tList[4], tList[5], tList[6]))
    myTurtle.pencolor((tList[4], tList[5], tList[6])) 
    myTurtle.turtlesize(tList[3])
    myTurtle.penup() 
    if index == 0 : 
        myTurtle.goto(tList[1], tList[2]) 
        continue 
    myTurtle.goto(sortedT[index-1][1], sortedT[index-1][2]) # 선을 그을 거북이를 이 전의 거북이 위치로 이동 
    myTurtle.pendown() 
    myTurtle.goto(tList[1], tList[2]) # 다음 거북이의 좌표로 이동하면서 선 긋기 

turtle.done()

