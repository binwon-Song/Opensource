def Translate(num):   #16진수에 맞춰 변환
    if num==10:
        return 'A'
    elif num==11:
        return 'B'
    elif num==12:
        return 'C'
    elif num==13:
        return 'D'
    elif num==14:
        return 'E'
    elif num==15:
        return 'F'
    elif 0<=num<=9:
        return str(num)
def ToBase2(number,Base2):  #2진수 변환
    if number==0 or number==1:  #더이상 못 나누면
        Base2+=str(number)
        PrintBase(Base2)
    else:
        Base2+=str(number%2);number=number//2   #나머지는 저장하고 몫은 다시 활용
        ToBase2(number,Base2)  #재귀호출
        
def ToBase8(number,Base8):  #8진수 변환
    if 0<=number<=7:
        PrintBase(Base8+str(number))
    else:
        Base8+=str(number%8);number=number//8
        ToBase8(number,Base8)
       ###### 2019038036   송빈원   ###### 
def ToBase16(number,Base16):  #16진수 변환
    if 0<=number<=15:
        PrintBase(Base16+Translate(number))
    else:
        Base16+=Translate(number%16);number=number//16
        ToBase16(number,Base16)
def PrintBase(Base):
    tmp=[]
    #문자열 거꾸로 호출
    for i in range(1,len(Base)+1):
        tmp.append(Base[-i])
    print(" ".join(tmp)+'\n')
    


Base10=int(input('10진수 입력 : '))
Base=""
print('2진수 : ',end='')
ToBase2(Base10,Base)
Base=""
print('8진수 : ',end='')
Base=ToBase8(Base10,Base)
Base=""
print('16진수 : ',end='')
Base=ToBase16(Base10,Base)
