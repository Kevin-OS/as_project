import scrapy


class RatesSpider(scrapy.Spider):
    name = "rates"

    def start_requests(self):
        urls = [
            'http://www.x-rates.com/table/?from=EUR&amount=1',
            'http://www.x-rates.com/table/?from=GBP&amount=1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        currency = response.css('td::text').extract()
        rate = response.css('td.rtRates a::text')[0::2].extract()
        count = 0
        for rate in rate:
            yield {
                'Currency': currency[count],
                'Rate': rate
            }
            count += 1