import requests
import re
import csv
url='https://maoyan.com/board'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
,'Cookie': 'uuid_n_v=v1; uuid=5C496E70B71311EBB66D1FD9F82B073E3F48ABC6FD6B48C69D953DD32A2176B5; _csrf=a3ee83e87f3d1484cf8d01faec334313ed8585ac8e01c67b0e2b52a2c61d83e8; _lxsdk_cuid=1797a80d8caaf-07cfd0227be071-c3f3568-1fa400-1797a80d8cbc8; _lxsdk=5C496E70B71311EBB66D1FD9F82B073E3F48ABC6FD6B48C69D953DD32A2176B5; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1621257935; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1621257948; __mta=188661655.1621257935308.1621257935308.1621257948461.2; _lxsdk_s=1797a80d8cb-0c2-24a-582%7C%7C6'
,'Upgrade-Insecure-Requests': '1'
,'Referer': 'https://maoyan.com/'}
response=requests.get(url,headers=headers)
print(response.text)
titles=re.findall('<div class="movie-item-info">.*?<p class="name"><a href="/films/.*?" title="(.*?)" data-act="boarditem-click',response.text,re.S)
actors=re.findall('<p class="star">(.*?)</p>',response.text,re.S)
scores1=re.findall('<i class="integer">(.*?)</i>',response.text,re.S)
scores2=re.findall('<i class="fraction">(.*?)</i>',response.text,re.S)
# for i in range(10):
#     print(scores1[i]+scores2[i])
# for actor in actors:
#     print(actor.strip().replace('主演：','').replace(',',' '))
# for title in titles:
#     print(title)
with open('maoyan1.csv','w',encoding='utf-8',newline='') as f:
    write=csv.writer(f)
    write.writerow(['title','actor','score'])
    for i in range(10):
        write.writerow([titles[i],actors[i].strip().replace('主演：','').replace(',',' '),scores1[i]+scores2[i]])