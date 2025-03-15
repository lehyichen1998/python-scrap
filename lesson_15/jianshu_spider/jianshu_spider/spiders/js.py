# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from spider.spider_demo.jianshu_spider.jianshu_spider.items import ArticleItem


class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath('//h1[@class="_1RuRku"]/text()').get()
        avatar = response.xpath('//a[@class="_1OhGeD"]/text()').get()
        author = response.xpath('//a[@class="_1OhGeD"]/text()').get()
        pub_time=response.xpath('//div[@class="s-dsoj"]/time/text()').get()
        article_id = response.url.split('/')[-1]
        content = response.xpath("//article[@class='_2rhmJa']").get()
        word_count=response.xpath("//div[@class='s-dsoj']/span[2]/text()").get()
        read_count=response.xpath("//div[@class='s-dsoj']/span[3]/text()").get()
        like_count=response.xpath("//span[@class='_1LOh_5']/text()").get()
        comment_count=",".join(response.xpath("//span[@class='_2R7vBo']/text()").getall())
        subjects=",".join(response.xpath("//div[@class='_2Nttfz']/a/span/text()").getall())


        item = ArticleItem(title=title,
                           content=content,
                           article_id=article_id,
                           pub_time=pub_time,
                           avatar=avatar,
                           author=author,
                           origin_url=response.url,
                           word_count=word_count,
                           read_count=read_count,
                           like_count=like_count,
                           comment_count=comment_count,
                           subjects=subjects
                           )
        yield item


