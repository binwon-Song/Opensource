import re

# 정규식

# 1. p.compile("정규식")
# 2. p.match("비교할 문자열")






re.compile("ca.e") 
# .은 하나의 문자
# ^은 문자열의 시작  (^de) desk,destination
# $은 문자열의 끝

def print_match(m):
    if m:
        print(m.group()) #매치 안되면 에러 발생
        print(m.string()) #입력받은 문자열
        print(m.start())  #일차흔 문자열의 시작 index
        print(m.end())  #일치하는 문자열의 끝 index
        print(m.span()) #일치하는 문자열의 시작/ 끝 index
    else:
        print('not match')

m=p.match('case')

# match : 처음부터 일치하는지 확인
# search : 주어진 문자열 중에 일치하는지 확인
# findall : 일치하는 모든 것을 리스트 형태로 반환
print_match(m)

