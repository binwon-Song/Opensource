import requests
import re
from bs4 import BeautifulSoup


header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

# for i in range(3):

for year in range(2015,2019):
    url='https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
    res=requests.get(url,headers=header)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'lxml')
    images=soup.find_all('img',attrs={'class':'thumb_img'})
    for idx, image in enumerate(images):
        image_url=image['src']
        if image_url.startswith('//'):
            iamge_url='https://'+image_url
        image_res=requests.get(image_url)
        image_res.raise_for_status()
        
        with open(f"movie_{year}_{idx+1}.jpg","wb") as f:
            f.write(image_res.content) #content 정보를 바로 파일로 사용
        if idx>=4:
            break