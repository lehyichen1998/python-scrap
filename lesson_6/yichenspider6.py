import requests
from lxml import etree

url = ['https://maoyan.com/board/4?offset=0',
       'https://maoyan.com/board/4?offset=10',
       'https://maoyan.com/board/4?offset=20']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Cookie': '__mta=150770953.1621258013213.1621431793006.1621431813350.17; uuid_n_v=v1; uuid=80C7C710B71311EB9148110DC3B2994760FB01FEEE7341FEB455812A0FCD84F7; _lxsdk_cuid=1797a820414c8-018cb8505dda1a-2363163-144000-1797a820414c8; _lxsdk=80C7C710B71311EB9148110DC3B2994760FB01FEEE7341FEB455812A0FCD84F7; _csrf=a369fbea9473b26254da0f271013a4d02862bf75a2d3dc3c64ef53a3b16cfdfc; __mta=150770953.1621258013213.1621424753596.1621425334542.9; _lxsdk_s=17984dc32d0-4bc-7aa-64f%7C%7C12'
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
    response = requests.get(url, headers=headers)
    return response.text


def parse_new_url_data(new_res):
    new_html = etree.HTML(new_res)
    dra = new_html.xpath('//span[@class="dra"]/text()')
    print(dra)


for i in url:
    response = get_data(i)
    names = parse_data(response)[0]
    time = parse_data(response)[1]
    new_url = parse_data(response)[2]
    for x in new_url:

        real_url = 'https://maoyan.com' + x
        print(real_url)
        new_res = get_new_url_data(real_url)
        # print(new_res)
        parse_new_url_data(new_res)
