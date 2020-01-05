import scrapy

class ReadAttributeSpider(scrapy.Spider):
    name= "read_attribute"

    def start_requests(self):
        tag = getattr(self, "tag", None)

        if tag is None:
            print("ENTER THE TAG VALUE!!!")
        else:
            start_urls = "http://quotes.toscrape.com/tag/" + tag
        yield scrapy.Request(start_urls, self.parse)

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')

        for i, quote in enumerate(quotes):
            yield{
            'id': i,
            'Quote': quote.xpath('span[@class="text"]/text()').get(),
            'Author': quote.xpath('span/small[@class="author"]/text()').get(),
             }
