# import requests
# from bs4 import BeautifulSoup

# url="https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Oct0121&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-mo-Evergreen-Oct0121-Text_Search_BKWS-BKWS%7cONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=Cj0KCQiA2NaNBhDvARIsAEw55hiIPjJiTx1nmmNVhQy-95y4oLSqwwRlQAgpEXyEyleIdYBvpR9BUx8aAlmUEALw_wcB&gclsrc=aw.ds"

# res=requests.get(url)
# res.raise_for_status()

# soup=BeautifulSoup(res.text,'lxml')

# movies=soup.find_all('div',attrs={'class':'DdYX5'})

# with open('movies.html',"w",encoding='utf8') as f:
#     f.write(soup.prettify)
import requests
from bs4 import BeautifulSoup

url='https://eis.cbnu.ac.kr/CBNU/index.html?16426462080'

res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml')

clsa=soup.find_all('div',attrs={'id':'mainframe_VFS_HFS_INVFS_WorkFrame_win_2275_form_div_work_grd_master_body_gridrow_4_cell_4_11'})

    # for c in clsa:
    #     name=c.find('div',attrs={'class':'name'}).get_text()
    #     price=item.find('strong',attrs={'class':'price-value'}).get_text()
    #     grade=item.find('em',attrs={'class':'rating'}).get_text()
    #     after=item.find('span',attrs={'class':'rating-total-count'}).get_text()
    #     print(name,price)
    #     print(grade,after )
a=clsa.find('title').get_text()
print(a)
