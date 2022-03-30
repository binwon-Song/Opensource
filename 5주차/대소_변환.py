
str=input()
new_str=[]
for i in range(len(str)):
    if str[i].isupper():
        new_str.append(str[i].lower())
    else:
        new_str.append(str[i].upper())
print("".join(new_str))

