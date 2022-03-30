import re
Long_sentence=input()
frequency={}
reg=re.compile('[a-zA-Z]')
for i in Long_sentence:
    if i not in frequency:
        if i.isalpha() and not reg.search(i):
            frequency[i]=1
    else:
        if i.isalpha() and not reg.search(i):
            frequency[i]+=1
    

sort_frequency=sorted(frequency.items(),key=lambda x:-x[1])
print('-------------------------')
print('문자\t빈도수')
print('-------------------------')
for i in sort_frequency:
    print(i[0],'\t',i[1])
    
