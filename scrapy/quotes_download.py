import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes_download'
    start_urls = [
    'http://quotes.toscrape.com/page/1/',
    #'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')

        for i, quote in enumerate(quotes):
            yield{
            'id': i,
            'Quote': quote.xpath('span[@class="text"]/text()').get(),
            'Author': quote.xpath('span/small[@class="author"]/text()').get(),
             }
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        print(next_page)
        if next_page is not None:
            #next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)
