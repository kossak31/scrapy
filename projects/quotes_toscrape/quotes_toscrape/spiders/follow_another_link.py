# -*- coding: utf-8 -*-
import scrapy


class ScrapyAnotherLinkDetails(scrapy.Spider):
    name = 'follow_another_link'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/', ]

    def parse(self, response):
        # get quotes
        quotes = response.css('div.quote')

        # get author links
        for quote in quotes:
            author_partial_link = quote.css(
                'span a::attr(href)').extract_first()
            author_link = response.urljoin(author_partial_link)

            # open links in author_link and run function parse_author
            yield scrapy.Request(author_link, callback=self.parse_author)

        # follow next page
        next_page_url = response.css('li.next a::attr(href)').extract_first()
        if next_page_url:
            next_page_absolute_url = response.urljoin(next_page_url)
            yield scrapy.Request(next_page_absolute_url, self.parse)

    # function parse_author
    def parse_author(self, response):
        name = response.css('h3.author-title::text').extract_first().strip()
        born_date = response.css(
            'span.author-born-date::text').extract_first().strip()
        born_location = response.css(
            'span.author-born-location::text').extract_first().strip()[3:]  # remove 3 chars "in "
        description = response.css(
            'div.author-description::text').extract_first().strip()

        yield {
            'name': name,
            'born_date': born_date,
            'born_location': born_location,
            'description': description,
        }
