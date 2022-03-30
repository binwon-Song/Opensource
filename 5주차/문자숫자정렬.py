number=["A37B","23CC","88D9","BB8F","3A9A"]
sort_number=[]
tmp=[]
for idx,i in enumerate(number):
    for j in i:
        if j.isdigit():
            tmp.append(j)
    sort_number.append([idx,int("".join(tmp))])
    tmp=[]
sort_number.sort(key=lambda x:x[1])
print('정렬 전 데이터 : '+" ".join(number))
print('정렬 후 데이터 : ',end='')
for i in sort_number:
    print(number[i[0]],end=' ')
print('\n')