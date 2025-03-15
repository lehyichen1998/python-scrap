'''
class dog():
    def dogspeak(self):
        print('dog talk')

    def dogrun(self):
        print('dog run')

    def dogeat(self):
        print('dog eating')


Dog = dog()
print(Dog)
'''

'''
import urllib.request
from urllib import request, parse

# url = 'https://www.python.org/'
url = 'https://www.baidu.com/s'
# data = bytes(urllib.parse.urlencode(({'wd': '大家好'}), encoding='utf-8'))
response = urllib.request.urlopen(url, timeout=10)
# response = urllib.request.urlopen('https://www.python.org/',timeout=10)
# print(response.read())
# print(type(response))
print(response.status)
'''

'''
from urllib.parse import urlparse

url = 'https://www.baidu.com/index.html;user?id=5#comment'
result = urlparse(url)
print(result)
'''

'''
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib import  error
params = {
    'wd': '你好'
}
try:
    # response = urlopen('https://www.baidu.com/s?wd=你好')
    response = urlopen('https://aaccs.com/index.html')
except error.URLError as e:
    print(e.reason)
url = 'https://www.baidu.com/s?' + urlencode(params)
print(url)
'''

'''
import requests

url = 'https://my.xiapibuy.com/api/v4/search/search_items?by=relevancy&keyword=watch&limit=50&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'cookie': 'REC_T_ID=da1bd2d6-6901-11eb-9f46-08f1ea7b58ac; SPC_IA=-1; SPC_EC=-; SPC_U=-; SPC_F=MjmY3voiAOKbynppATsB04b1d8apYrci; REC_T_ID=da256412-6901-11eb-8ead-48df3757ce60; language=zhHans; _gcl_au=1.1.1442129308.1620655090; _med=refer; csrftoken=7wO6Yek6218QgBVIjrLWEECBzj1TeRYd; SPC_SI=mall.3VbBfmgAOaIBV5ixVRz1KGpoEjBvJZh5; welcomePkgShown=true; SPC_R_T_ID="mP6W/Jk5dsxh6ZqLo4wLoQ9lE7jwervpZYWGa1jitZXN6hWKM74/4ErPZvhqt4r+CvIHftIrLPOVEgIbfAegaxkrWWgrQhObCsZ683f0xcU="; SPC_T_IV="JhXtVG9Xih2P6Faua+FjNw=="; SPC_R_T_IV="JhXtVG9Xih2P6Faua+FjNw=="; SPC_T_ID="mP6W/Jk5dsxh6ZqLo4wLoQ9lE7jwervpZYWGa1jitZXN6hWKM74/4ErPZvhqt4r+CvIHftIrLPOVEgIbfAegaxkrWWgrQhObCsZ683f0xcU="'
}
response = requests.get(url, headers=headers)
print(response.text)
'''
'''
import requests

url='https://s.taobao.com/search?q=watch&type=p&tmhkh5=&spm=a2141.241046-my.a2227oh.d100&from=sea_1_searchbutton&catId=100'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'cookie':'thw=my; cna=51wyGPLJOkECAXl6U9y1bUj4; hng=MY%7Czh-CN%7CMYR%7C458; fbm_824328494287859=base_domain=.taobao.com; tracknick=tb156605338; miid=588561402137054127; enc=1aBDyQcOJAoqH1L9gq6rWtpih9cHxVDEgQU8%2BVdPzAQbzTKgPJwxb7TCx7kK1OEtu3qbM98Zyu5SwYq5c9pOmSBLq6k8sn4nbwDcG%2BOVi4A%3D; sgcookie=E100Ga%2FVVkfR8JGRRWryq6VVpzwnQ6RiE5cPwBI9BoZHiS4Rddx9HqIj4QfPQDbbonbNzb%2FO6Yi%2BiWr5j7R1IQxu3w%3D%3D; _cc_=U%2BGCWk%2F7og%3D%3D; _m_h5_tk=c494ecab39cd0f222094a76243125be5_1620664930385; _m_h5_tk_enc=88a5074d5484e9a3ba5189b3a0972458; mt=ci=-1_0; uc1=cookie14=Uoe2zXwcof%2BHIQ%3D%3D; cookie2=1548121a8dbd7ec24c3688ce0dc5e4f6; t=8aa8bf7014ebc7731d562b6af4119fb8; _tb_token_=711b8e8516457; xlly_s=1; JSESSIONID=7C6B68E3BF69D356069E2EB7E967DD88; alitrackid=world.taobao.com; lastalitrackid=world.taobao.com; tfstk=cidGBSb6xdW_XI6HFf16WLnHWjlRwUDNfIReTIRI5tx3pJ10WJyPMKghXhAYh; l=eBNeG2BuOng5BGESBOfanurza77OSIRYYuPzaNbMiOCP_P5B55VCW6614dY6C3GNh6HJR3-IkQOyBeYBqQAonxv92j-la_kmn; isg=BJCQTofVxIp5e6e7juq40k-XYd7iWXSjBuB6EophXOu-xTBvMmlEM-b3mIUlICx7'
}
response= requests.get(url,headers=headers)
print(response.text)
'''

import requests

url = 'https://shopee.com.my/api/v4/search/search_items?by=relevancy&keyword=watch&limit=50&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'cookie': 'REC_T_ID=57946d7c-376f-11eb-b145-08f1ea7b48c8; SPC_EC=-; SPC_IA=-1; SPC_U=-; SPC_F=6nryLr3SNtMfoeGxR5v0yG2UU7wJ1GJq; language=zhHans; _gcl_aw=GCL.1620391582.Cj0KCQjwytOEBhD5ARIsANnRjVimdft-AzXC4Cu4u3KgynA01Q8HeFOd2ySHbpCuGtiSPiMTXjzpWyMaApWEEALw_wcB; _gcl_au=1.1.410984046.1620391582; _med=refer; csrftoken=JPAGdwVfoQXCtoevw67aen21oap9UgGD; SPC_SI=mall.Y5GS01JmPS1AX1XfBeotofv06qd7LdsX; welcomePkgShown=true; SPC_R_T_ID="2rD4lv/dcLx5SZ4eTzzLZWxPqsECkzgU7Db0CZ8cxNiwGUtPKGYFf15zEwn3Z4NopSQxapzk/xgmUzwX5Yne6cQ7XpqlyFyP4mVtCbyQKhs="; SPC_T_IV="JL7b4y+n5TnZYdDc4w767w=="; SPC_R_T_IV="JL7b4y+n5TnZYdDc4w767w=="; SPC_T_ID="2rD4lv/dcLx5SZ4eTzzLZWxPqsECkzgU7Db0CZ8cxNiwGUtPKGYFf15zEwn3Z4NopSQxapzk/xgmUzwX5Yne6cQ7XpqlyFyP4mVtCbyQKhs="'
}
response = requests.get(url, headers=headers)
print(response.text)
