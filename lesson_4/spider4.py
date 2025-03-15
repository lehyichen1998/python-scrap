import requests
import re
import csv

url = 'https://my.xiapibuy.com/api/v4/search/search_items?by=relevancy&keyword=shoes&limit=50&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'
headers = {
    'cookie': 'REC_T_ID=da1bd2d6-6901-11eb-9f46-08f1ea7b58ac; SPC_IA=-1; SPC_EC=-; SPC_U=-; SPC_F=MjmY3voiAOKbynppATsB04b1d8apYrci; REC_T_ID=da256412-6901-11eb-8ead-48df3757ce60; language=zhHans; _gcl_au=1.1.1442129308.1620655090; _med=refer; csrftoken=1ieew3m14BXAHLkOvkQtxY8a6tq9n4lI; SPC_SI=mall.gu2ED4rYUnSAfY1Ye8AelTjkBtUCu85B; welcomePkgShown=true; SPC_R_T_ID="lcAlt74vh1ZmiN/79h8Ls1amxITYJx8aU8/4BMKdYJoqeLPqb1AkAROSO/Ly2jwrLzdMzMdpFT1KSLpJVdcf4kbaRZV+KIl2p+WBXKr/QKg="; SPC_T_IV="kUKhcoDp1bNJFVwF/q3fsw=="; SPC_R_T_IV="kUKhcoDp1bNJFVwF/q3fsw=="; SPC_T_ID="lcAlt74vh1ZmiN/79h8Ls1amxITYJx8aU8/4BMKdYJoqeLPqb1AkAROSO/Ly2jwrLzdMzMdpFT1KSLpJVdcf4kbaRZV+KIl2p+WBXKr/QKg="',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

response = requests.get(url, headers=headers)
# print(response.text)
prices = re.findall('"item_status":"normal","price":(.*?),"price_min":.*?,"price_max"', response.text, re.S)
num1 = 0
for i in prices:
    num1 += 1
    print(num1, '.', i)

result = re.findall('shopid":.*?,"name":(.*?),"label_ids":.*?', response.text, re.S)
num2 = 0
for i in result:
    num2 += 1
    print(num2, '.', i)

with open('shopee_Data.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'price'])
    for i in range(50):
        writer.writerow([result[i], int(prices[i])/100000])
