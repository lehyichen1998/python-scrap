import scrapy
import re


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    def parse(self, response, **kwargs):
        information_list = response.xpath("//dl[@class='board-wrapper']/dd")
        for information in information_list:
            item = {}
            item['name'] = information.xpath('./div[1]/div[1]/div[1]/p/a/text()').extract_first()
            item['star'] = information.xpath('./div[1]/div[1]/div[1]/p[2]/text()').extract_first().strip()
            yield item
        list_url = response.xpath("//ul[@class='list-pager']/li").extract()
        new_url = re.findall(' href="(.*?)"', list_url[-1], re.S)
        next_url = 'https://maoyan.com/board/4' + new_url[0]
        url = response.urljoin(next_url)
        yield scrapy.Request(url=url, callback=self.parse)
