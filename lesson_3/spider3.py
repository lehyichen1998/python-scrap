import requests

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

'''
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'cookie': '_gcl_au=1.1.1445177354.1619177862; _med=refer; SPC_IA=-1; SPC_EC=-; SPC_U=-; REC_T_ID=63f95a3e-a428-11eb-b6b1-b4969197e5a8; REC_T_ID=63fe25d9-a428-11eb-9621-2cea7f4af375; SPC_F=CeY9areYf6SttUDDHwqJMBCVIVHGyw81; language=en; SPC_SI=mall.WXugrFnWey7PxzdcFTVgeqdhcPBDUtC1; csrftoken=47vVMUOihQQkLzGiafYa4Nw4oPbNGfQ4; welcomePkgShown=true; SPC_R_T_ID="01YjN44teQL0JlsoQcOIM2gEnWVaCXSR5qRvC7cVPtHC4SSGQ9JCpcsC5VFTxgrJ9D3FiPOHBCzLrtKT8lbI+xu0t4Ku5IUS6U3Z8PRjiTo="; SPC_T_IV="cfy0Sd4A8MtZ676s6DUQ5w=="; SPC_R_T_IV="cfy0Sd4A8MtZ676s6DUQ5w=="; SPC_T_ID="01YjN44teQL0JlsoQcOIM2gEnWVaCXSR5qRvC7cVPtHC4SSGQ9JCpcsC5VFTxgrJ9D3FiPOHBCzLrtKT8lbI+xu0t4Ku5IUS6U3Z8PRjiTo="'}

r = requests.get('https://cf.shopee.com.my/file/bcc80587c2f9c55eb7b765e9196dc686_tn', headers=header)
with open('shopee.png', 'wb') as f:
    f.write(r.content)
# print(r.content)
'''

'''
def students(num, speak):
    x = num + 3
    y = speak + 1
    print(x, y)
students(4, 6)
'''

'''
files = {'file': open('shopee.png', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
'''

'''
q = requests.Session()
q.get('http://httpbin.org/cookies/set/number/123456789')
r = q.get('http://httpbin.org/cookies')
print(r.text)
'''




