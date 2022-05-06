import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)  #url에 대한 정보를 전달
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml") 

# print(soup.title)
# print(soup.title.get_text)
# print(soup.a)   soup객체 에서 처음 발견되는 a element
# print(so up.a.attrs)  #a element의 속성 정보를 출력
# print(soup.a['href'])  href 속성 값 출력

# print(soup.find('a',attrs={'class':'Nbtn_upload'}))
# print(soup.find(attrs={'class':'Nbtn_upload'}))

rank1=soup.find('li',attrs={'class':'rank01'})
# print(rank1.a.get_text)
# rank2=rank1.next_sibling.next_sibling
# rank1=rank2.previous_sibling.previous_sibling
#  print(rank1.parent)
# rank2=rank1.find_next_sibling('li')
# print(rank2.a.get_text())

# print(rank1.find_next_siblings('li'))

# webtoon=soup.find('a',text='신의 탑')
# print(webtoon)