# -*- coding: utf-8 -*-
import scrapy


class MainSpiderSpider(scrapy.Spider):
    name = 'main_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # get quotes
        quotes = response.css('div.quote')

        # getall quotes
        for quote in quotes:
            text = quote.css('span.text::text').getall()
            author = quotes.css('small.author::text').getall()
            tags = quote.css('div.tags a::text').getall()

            yield {
                'Quote': text,
                'Author': author,
                'Tags': tags
            }

        # pagination next button
        next_page_url = response.css('li.next a::attr(href)').extract_first()
        if next_page_url:
            next_page_absolute_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_absolute_url, self.parse)

        # another way to pagination next button without urljoin
        # next_page_url = response.css('li.next a::attr(href)').extract_first()
        # if next_page_url:
            # next_page_absolute_url = 'http://quotes.toscrape.com/' + next_page_url
            # yield scrapy.Request(next_page_absolute_url, self.parse)
