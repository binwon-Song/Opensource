import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=675554"
res=requests.get(url)  #url에 대한 정보를 전달
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")


cartoons=soup.find_all('td',attrs={'class':'title'})
# title=cartoons[0].a.get_text()
# link=cartoons[0].a['href']
# print(title)
# print(link)
# 회차 정보 표시
for cartoon in cartoons:
    title=cartoon.a.get_text()
    link='https://comic.naver.com'+cartoon.a['href']
    print(title,link)

# 평점 정보 표시 및 평점 평균 계산
stars=soup.find_all('div',attrs={'class':'rating_type'})
count=[]
for star in stars:
    grade=star.strong.get_text()   #grade.find('strong').get_text()
    print(grade)
    count.append(float(grade))

print('평점 평균 : ',sum(count)/len(count))

