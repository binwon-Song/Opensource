import requests
res=requests.get("https://nadocoding.tistory.com")
res.raise_for_status()

with open('coding.html','w',encoding='utf8') as f:
    f.write(res.text)