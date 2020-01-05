import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author_spider'

    start_urls = ["http://quotes.toscrape.com"]

    def parse_author(self, response):
        yield {
         'name': response.xpath('//h3[@class="author-title"]/text()').get(),
         'dob' : response.xpath('//span[@class="author-born-date"]/text()').get(),
         'birth_place': response.xpath('//span[@class="author-born-location"]/text()').get()[3:],
         'info': response.xpath('//div[@class="author-description"]/text()').get()

        }

    def parse(self, response):
        #response.xpath('//div[@class="quote"]/span/a/@href').get()
        #response.xpath('//span/small[@class="author"]/text()').get()

        author_links = response.xpath('//div[@class="quote"]/span/a/@href').getall()

        for author_link in author_links:
            yield response.follow(author_link, self.parse_author)

        next_page = response.xpath('//li[@class="next"]/a/@href').get()

        if next_page is not None:
            #next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)
