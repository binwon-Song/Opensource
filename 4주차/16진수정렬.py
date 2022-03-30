def selected_sort(num,number):
    for j in range(num):        #배열의 크기만큼 루프
        min_idx=j               #최저 인덱스 가정
        for i in range(j+1,num):
            if number[min_idx]>number[i]:   #최저값 찾기
                min_idx=i                   #최저 인덱스 설정
        number[j],number[min_idx]=number[min_idx],number[j]     #스왑핑

num=int(input('정렬 할 데이터의 크기를 입력하세요.'))
number=input('정렬 할 데이터를 입력하세요. ').split()                  #데이터를 공백를 중십으로 입력받는다

#######################  2019038036_송빈원   ###########################

for i in range(num):
    number[i]=int(number[i],16)     #16진수 데이터를 10진수 데이터로 바꾼다

selected_sort(num,number)           #선택정렬
for i in range(num):
    number[i]=("{0:x}".format(number[i])).upper()


print(" ".join(number))
