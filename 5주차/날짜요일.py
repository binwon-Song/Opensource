from datetime import time,datetime

PrevDate=input("날짜 입력 '/'로 구분 ").split('/')    #날짜 입력받음
PrevDate="".join(PrevDate) 
CurrentDate=datetime.now()  #현재 날짜
PrevDate=datetime.strptime(PrevDate,"%Y%m%d")  #년 월 일 로 나눔

DateDiff=CurrentDate-PrevDate       #
week=datetime.weekday(CurrentDate)  #요일
weekDay=""
if week==0:
    weekDay="월요일"
elif week==1:
    weekDay="화요일"
elif week==2:
    weekDay="수요일"
    ###### 2019038036   송빈원   ######
elif week==3:
    weekDay="목요일"
elif week==4:
    weekDay="금요일"
elif week==5:
    weekDay="토요일"
elif week==6:
    weekDay="일요일"
    
    
print(f"일 수 차이 : {DateDiff.days} 현재 요일은 : {weekDay}")
