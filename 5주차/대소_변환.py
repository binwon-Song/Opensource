
str=input()
new_str=[]
for i in range(len(str)):
    if str[i].isupper():
        new_str.append(str[i].lower())   #대문자면 소문자로
    else:
        new_str.append(str[i].upper())  #소문자면 대문자로
print("".join(new_str))

###### 2019038036   송빈원   ######
