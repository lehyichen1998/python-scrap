import requests
import re
import csv

url = 'https://maoyan.com/board'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Cookie': 'uuid_n_v=v1; uuid=80C7C710B71311EB9148110DC3B2994760FB01FEEE7341FEB455812A0FCD84F7; _lxsdk_cuid=1797a820414c8-018cb8505dda1a-2363163-144000-1797a820414c8; _lxsdk=80C7C710B71311EB9148110DC3B2994760FB01FEEE7341FEB455812A0FCD84F7; _csrf=a369fbea9473b26254da0f271013a4d02862bf75a2d3dc3c64ef53a3b16cfdfc; __mta=150770953.1621258013213.1621259196534.1621424628715.7; _lxsdk_s=17984705a91-d9c-db0-38b%7C%7C3',
    'Host': 'maoyan.com',
    'Pragma': 'no-cache',
    'Referer': 'https://maoyan.com/'
}

response = requests.get(url, headers=headers)
print(response.text)

titles = re.findall(
    '<div class="movie-item-info">.*?<p class="name"><a href="/films/.*?" title="(.*?)" data-act="boarditem-click',
    response.text, re.S)
actors = re.findall('<p class="star">(.*?)</p>', response.text, re.S)
scores1 = re.findall('<i class="integer">(.*?)</i>', response.text, re.S)
scores2 = re.findall('<i class="fraction">(.*?)</i>', response.text, re.S)
# for title in titles:
#     print(title)
# for actor in actors:
#     print(actor.strip().replace('主演：', '').replace(',', ' '))
# for i in range(10):
#     print(scores1[i]+scores2[i])


with open('maoyan1.csv', 'w', encoding='utf-8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['title', 'actor', 'score'])
    for i in range(10):
        writer.writerow([titles[i], actors[i].strip().replace('主演:', '').replace(',', ' '), scores1[i] + scores2[i]])

# titles=re.findall('<div&nbsp;class="movie-item-info">.*?<p&nbsp;class="name"><a&nbsp;href="/films/.*?"&nbsp;title="(.*?)"&nbsp;data-act="boarditem-click',response.text,re.S)
# 指环王
