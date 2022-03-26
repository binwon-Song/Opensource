train_TL=[('토마스',5),('헨리',8),('에드워드',9),('에밀리',5),('토마스',4),('헨리',7),('토마스',3),('에밀리',8),('퍼시',5),('고든',13)]
train_D={};train_L=[]

for i in train_TL:
    if i[0] not in train_D:
        train_D[i[0]]=i[1]
    else:
        train_D[i[0]]+=i[1]

for key,value in train_D.items():
    train_L.append((key,value))
train_L.sort(key=lambda x:-x[1])
rank=[i for i in range(1,len(train_L)+1)]
######### 2019038036_송빈원
for i in range(1,len(train_L)):
    if train_L[i][1]==train_L[i-1][1]:
        rank[i]-=1
    else:
        pass
print('기차     총수송량  순위')
print('------------------------------')
for index,i in enumerate(train_L):
    print(f"{i[0]:<7}{i[1]:<7}{rank[index]:<7}")



