import requests
from lxml import etree

url = ['https://maoyan.com/board/4?offset=0',
       'https://maoyan.com/board/4?offset=10',
       'https://maoyan.com/board/4?offset=20']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Cookie': '__mta=150770953.1621258013213.1621433066324.1621598994745.19; uuid_n_v=v1; uuid=80C7C710B71311EB9148110DC3B2994760FB01FEEE7341FEB455812A0FCD84F7; _lxsdk_cuid=1797a820414c8-018cb8505dda1a-2363163-144000-1797a820414c8; _lxsdk=80C7C710B71311EB9148110DC3B2994760FB01FEEE7341FEB455812A0FCD84F7; __mta=150770953.1621258013213.1621424753596.1621425334542.9; _csrf=faa3c1ad87990a6dcc3ebbb809b9484a977ecba239025b85eb478bb78350d406; _lxsdk_s=1798ed4faf2-841-805-483%7C%7C2'
}


def get_data(url):
    response = requests.get(url, headers=headers)
    return response.text


def parse_data(res):
    html = etree.HTML(res)
    names = html.xpath('//p[@class="name"]/a/text()')
    times = html.xpath('//p[@class="releasetime"]/text()')
    new_url = html.xpath('//p[@class="name"]/a/@href')

    return names, times, new_url


def get_new_url_data(url):
    new_res = []
    response = requests.get(url, headers=headers)
    new_res.append(response.text)
    return new_res


def parse_new_url_data(new_res):
    for res in new_res:
        new_html = etree.HTML(res)
        dra = new_html.xpath('//span[@class="dra"]/text()')
        print(dra)



for i in url:
    response = get_data(i)
    names = parse_data(response)[0]
    time = parse_data(response)[1]
    new_url = parse_data(response)[2]
    for x in new_url:
        real_url = 'https://maoyan.com' + x
        new_res = get_new_url_data(real_url)
        for i in new_res:
            parse_new_url_data(i)

# for i in url:
#     response = get_data(i)
#     # print(response)
#     result = parse_data(response)
#     names = result[0]
#     times = result[1]
#     new_urls = result[2]
#     for new_url in new_urls:
#         new_res = get
#     # print(names)
#     # print(new_urls)
#     # print(times)
#     break
