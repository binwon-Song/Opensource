import requests
import re
from bs4 import BeautifulSoup


header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

for i in range(5):
    url="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)

    res=requests.get(url,headers=header)
    res.raise_for_status()

    soup=BeautifulSoup(res.text,'lxml')

    itmes=soup.find_all('li',attrs={'class':re.compile('^search.product')})

    for item in itmes:
        name=item.find('div',attrs={'class':'name'}).get_text()
        price=item.find('strong',attrs={'class':'price-value'}).get_text()
        grade=item.find('em',attrs={'class':'rating'}).get_text()
        after=item.find('span',attrs={'class':'rating-total-count'}).get_text()
        print(name,price)
        print(grade,after )

