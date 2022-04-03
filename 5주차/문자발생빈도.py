import re
Long_sentence=input()
frequency={}
reg=re.compile('[a-zA-Z]')
for i in Long_sentence:    #문자열 차례로 입력
    if i not in frequency:  #딕셔너리에 없으면
        if i.isalpha() and not reg.search(i): #한글이면서 영어가 아닌 경우
            frequency[i]=1
    else:
        if i.isalpha() and not reg.search(i):
            frequency[i]+=1                     #딕셔너리에 들어가있으면 +1
    
###### 2019038036   송빈원   ######
sort_frequency=sorted(frequency.items(),key=lambda x:-x[1])  #숫자를 기준으로 정렬
print('-------------------------')
print('문자\t빈도수')
print('-------------------------')
for i in sort_frequency:
    print(i[0],'\t',i[1])       #빈도수 출력
    
