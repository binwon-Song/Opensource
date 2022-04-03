number=["A37B","23CC","88D9","BB8F","3A9A"]
sort_number=[]
tmp=[]
for idx,i in enumerate(number):   #인덱스 값과 number값 받음
    for j in i:
        if j.isdigit():   #문자열 인덱스가 숫자면
            tmp.append(j)       #저장
    sort_number.append([idx,int("".join(tmp))]) #기존 인덱스와 숫자값 append
    tmp=[]
###### 2019038036   송빈원   ######
sort_number.sort(key=lambda x:x[1])         #숫자 기준으로 정렬
print('정렬 전 데이터 : '+" ".join(number))
print('정렬 후 데이터 : ',end='')
for i in sort_number:
    print(number[i[0]],end=' ')         
print('\n')