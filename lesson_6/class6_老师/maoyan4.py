import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    , 'Host': 'maoyan.com',
    'Referer': 'https://maoyan.com/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': '__mta=188661655.1621257935308.1621433014304.1621433022858.41; uuid_n_v=v1; uuid=5C496E70B71311EBB66D1FD9F82B073E3F48ABC6FD6B48C69D953DD32A2176B5; _lxsdk_cuid=1797a80d8caaf-07cfd0227be071-c3f3568-1fa400-1797a80d8cbc8; _lxsdk=5C496E70B71311EBB66D1FD9F82B073E3F48ABC6FD6B48C69D953DD32A2176B5; _csrf=8cc5231e67a52b75cc928004151cf116fa0dc6512bf556a730bf585d4fd4e45e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1621257935,1621261016,1621425511; __mta=188661655.1621257935308.1621429523012.1621430908744.20; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1621433023; _lxsdk_s=179847ddbca-46d-7dc-72b%7C%7C132'}

url=['https://maoyan.com/board/4?requestCode=106539865f8f209a752c2fc9dfd952e1iz371&offset=0'
     ,'https://maoyan.com/board/4?requestCode=106539865f8f209a752c2fc9dfd952e1iz371&offset=10'
     ,'https://maoyan.com/board/4?requestCode=106539865f8f209a752c2fc9dfd952e1iz371&offset=20']
def get_data(url): #这里获取最开始的数据

    response = requests.get(url, headers=headers)
    return response.text
def parse_data(res):#这里解析最开始的数据
    html = etree.HTML(res)
    names = html.xpath('//p[@class="name"]/a/text()')
    times = html.xpath('//p[@class="releasetime"]/text()')
    new_urls = html.xpath('//p[@class="name"]/a/@href')
    return names,times,new_urls
def get_new_url_data(url):#这里得到最新的数据
    new_res=[]
    response = requests.get(real_url, headers=headers)
    new_res.append(response.text)
    return new_res
def parse_new_url_data(new_res):#这里解析最新的数据
    for res in new_res:
        new_html = etree.HTML(res)
        dra = new_html.xpath('//span[@class="dra"]/text()')
        print(dra)


for i in url:
    response=get_data(i)
    names=parse_data(response)[0]
    times=parse_data(response)[1]
    new_url=parse_data(response)[2]
    for x in new_url:
        real_url = 'https://maoyan.com' + x
        new_res=get_new_url_data(real_url)
        parse_new_url_data(new_res)



