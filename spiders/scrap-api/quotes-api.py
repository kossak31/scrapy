# -*- coding: utf-8 -*-
import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        # get api full request
        # print(response.body)
        resp = json.loads(response.body)
        quotes = resp.get('quotes')
        for quote in quotes:
            yield {
                #ref author->name:
                'author': quote.get('author').get('name'),
                #ref tags:
                'tags': quote.get('tags'),
                #ref text
                'quote_text': quote.get('text')
            }
        #ref has_next: true
        has_next = resp.get('has_next')
        if has_next:
            #incrementa + 1 na ref page: 1
            next_page = resp.get('page') + 1
            yield scrapy.Request(
                url=f'https://quotes.toscrape.com/api/quotes?page={next_page}',
                callback=self.parse
            )