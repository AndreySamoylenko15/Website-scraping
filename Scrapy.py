import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mongoengine import Document, StringField, ListField, connect
import configparser


class MongoDBPipeline:
    def process_item(self, item, spider):
        if 'fullname' in item:
            author = Author(**item)
            author.save()
        else:
            quote = Quote(**item)
            quote.save()
        return item

class Author(Document):
    fullname = StringField(max_length=50)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField(max_length=4000)

class Quote(Document):
    tags = ListField(StringField(max_length=50))
    quote = StringField(max_length=1050)
    author = StringField(max_length=50)


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {
        'ITEM_PIPELINES': {
            '__main__.MongoDBPipeline': 300,
        }
    }

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                "tags": quote.css('div.tags a.tag::text').extract(),
                "author": quote.css('span small.author::text').extract_first(),
                "quote": quote.css('span.text::text').get()
            }

        next_link = response.css('li.next a::attr(href)').get()
        if next_link:
            yield scrapy.Request(url=response.urljoin(next_link), callback=self.parse)


def connect_to_db():
   connect(db='hw8', host='mongodb://localhost:27017')
if __name__ == "__main__":
    connect_to_db()
    process = CrawlerProcess(get_project_settings())
    process.crawl(QuotesSpider)
    process.start()