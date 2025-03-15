from bs4 import BeautifulSoup
import requests
url='https://maoyan.com/board/6'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
,
'Cookie': '__mta=188661655.1621257935308.1621261022715.1621426893256.6; uuid_n_v=v1; uuid=5C496E70B71311EBB66D1FD9F82B073E3F48ABC6FD6B48C69D953DD32A2176B5; _lxsdk_cuid=1797a80d8caaf-07cfd0227be071-c3f3568-1fa400-1797a80d8cbc8; _lxsdk=5C496E70B71311EBB66D1FD9F82B073E3F48ABC6FD6B48C69D953DD32A2176B5; _csrf=8cc5231e67a52b75cc928004151cf116fa0dc6512bf556a730bf585d4fd4e45e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1621257935,1621261016,1621425511; __mta=188661655.1621257935308.1621261022715.1621425511639.6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1621426893; _lxsdk_s=179847ddbca-46d-7dc-72b%7C%7C5'}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,'html5lib')
titles=soup.find_all(name='p',attrs='name')
actors=soup.find_all('p','star')
for i in range(10):
    print(actors[i].string)
# for i in range(10):
#     print(titles[i].a.string)
