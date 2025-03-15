# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        with open('maoyan.csv', 'a', encoding='utf-8', newline='')as file:
            fieldname = ['name', 'star']
            writer = csv.DictWriter(file, fieldnames=fieldname)
            writer.writeheader()
            writer.writerow(item)
        return item
