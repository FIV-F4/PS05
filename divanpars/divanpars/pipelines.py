# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

"""
class DivanparsPipeline:
    def process_item(self, item, spider):
        return item

"""
import csv

class CsvWriterPipeline:
    def open_spider(self, spider):
        self.file = open('items.csv', 'w', newline='')
        self.writer = csv.writer(self.file)
        # Записываем заголовки колонок
        self.writer.writerow(['name', 'price', 'url'])  # Замените на ваши имена колонок

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        # Записываем строку данных
        self.writer.writerow([item['name'], item['price'], item['url']])  # Замените на ваши поля
        return item
