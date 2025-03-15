from lxml import etree
import requests
import csv
url='https://maoyan.com/board'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
,'Host':'maoyan.com',
'Referer':'https://maoyan.com/',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Cookie':'__mta=19360135.1621229699619.1621232605407.1621233615312.18; uuid_n_v=v1; uuid=9D5AB640B6D111EB92E297064163C32DAB9FB285B447472289C8C36C4594B6C7; _lxsdk_cuid=17978d1fb8689-032c049c2944-5771133-e1000-17978d1fb87c8; _lxsdk=9D5AB640B6D111EB92E297064163C32DAB9FB285B447472289C8C36C4594B6C7; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; recentCis=883%3D165%3D332%3D150%3D1; _csrf=b5882b07f344eb59866902f27ea243d9c163d190850eefba777b055f6ef40a20; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1621229698,1621231348,1621233637; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1621234490; __mta=19360135.1621229699619.1621233615312.1621234490166.19; _lxsdk_s=17978d1fb87-d71-c77-f99%7C%7C71'
}
response=requests.get(url,headers=headers)
print(response.status_code)
html=etree.HTML(response.text)
result=etree.tostring(html,encoding='utf-8')
titles=html.xpath('//p[@class="name"]/a/text()')
actors=html.xpath('//p[@class="star"]/text()')
scores1=html.xpath('//p[@class="score"]/i[@class="integer"]/text()')
scores2=html.xpath('//p[@class="score"]/i[@class="fraction"]/text()')
with open('movielxml.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'actor','grade'])
    for i in range(10):
        writer.writerow([titles[i], actors[i].strip().replace('主演：',''),scores1[i]+scores2[i]])
# print(result.decode('utf8'))