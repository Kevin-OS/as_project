import scrapy

class RatesSpider(scrapy.Spider):
    name = "rates"

    def start_requests(self):
        urls = [
            'http://www.x-rates.com/table/?from=EUR&amount=1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'rates.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)