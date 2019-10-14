# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class argSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ('http://quotes.toscrape.com/login',)
 
    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token,
                                                   'password': '',
                                                   'username': ''},
                                         callback=self.scrape_pages)
 
    def scrape_pages(self, response):
        open_in_browser(response)


    # def startRequests(self):
    #     start_urls = ['http://www.woodyhooten.com']

    #     for url in start_urls:
    #         yield scrapy.Request(url=url, callback = self.parse)

    # def parse(self, response):
    #     title = response.css('title::text').extract()
    #     yield {'titletext': title}
        
        
        
        
        # # page = response.url.split("/")[-2]   # might cause some issues since the example urls were different in structure
        # filename = 'scraped.txt'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

