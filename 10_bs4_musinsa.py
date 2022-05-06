import requests
from bs4 import BeautifulSoup


header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

url=f"https://www.musinsa.com/category/003004?d_cat_cd=003004&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page=1&display_cnt=90&sale_goods=&group_sale=&kids=N&ex_soldout=&color=&price1=&price2=&exclusive_yn=&shoeSizeOption=&tags=&campaign_id=&timesale_yn=&q=&includeKeywords=&measure="
res=requests.get(url,headers=header)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')
itmes=soup.find_all('li',attrs={'class':'li_box'})
for item in itmes:
    name=item.find('p',attrs={'class':'item_title'}).get_text()
    price=item.find('p',attrs={'class':'price'}).get_text()
    rate_cnt=item.find('span',attrs={'class':'count'}).get_text()
    print(f"{name} {price}  {rate_cnt}")

