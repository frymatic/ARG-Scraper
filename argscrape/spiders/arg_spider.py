# -*- coding: utf-8 -*-
import scrapy


class argSpider(scrapy.Spider):
    name = 'argSpider'
    # allowed_domains = ['divvy.com']
    start_urls = [
        # 'http://quotes.toscrape.com/',
        # 'http://www.woodyhooten.com',
        'https://app.divvy.co/companies/Q29tcGFueTozMzc4/home'
        ]


    # def startRequests(self):
    #     start_urls = ['http://www.woodyhooten.com']

    #     for url in start_urls:
    #         yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext': title}
        
        
        
        
        # # page = response.url.split("/")[-2]   # might cause some issues since the example urls were different in structure
        # filename = 'scraped.txt'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

