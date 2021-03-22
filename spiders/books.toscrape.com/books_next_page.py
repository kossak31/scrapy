# -*- coding: utf-8 -*-
import scrapy


class BooksNextPageSpider(scrapy.Spider):
    name = 'books_next_page'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    
    base_url = 'http://books.toscrape.com/'

    def parse(self, response):
        all_books = response.xpath('//article[@class="product_pod"]')

        for book in all_books:
            # book link
            book_url = book.xpath('.//h3/a/@href').extract_first()

            # add catalogue/ to book link
            if 'catalogue/' not in book_url:
                book_url = 'catalogue/' + book_url

            # build new URL http://books.toscrape.com/catalogue/you-cant-bury-them-all-poems_961/
            book_url = self.base_url + book_url

            # scrap books, run function parse_book
            yield scrapy.Request(book_url, callback=self.parse_book)

        # follow next page
        next_page_partial_url = response.css(
            'li.next a::attr(href)').extract_first()
        
        # build new URL http://books.toscrape.com/catalogue/page-2.html
        if next_page_partial_url:
            if 'catalogue/' not in next_page_partial_url:
                next_page_partial_url = "catalogue/" + next_page_partial_url

            # http://books.toscrape.com/catalogue/page-2.html
            next_page_url = self.base_url + next_page_partial_url
            
            # scrap link next pages
            yield scrapy.Request(next_page_url, callback=self.parse)

    # scrap book individual page
    def parse_book(self, response):
        title = response.xpath('//div/h1/text()').extract_first()

        relative_image = response.xpath(
            '//div[@class="item active"]/img/@src').extract_first()
        final_image = self.base_url + relative_image.replace('../..', '')

        price = response.xpath(
            '//div[contains(@class, "product_main")]/p[@class="price_color"]/text()').extract_first()
        stock = response.xpath(
            '//div[contains(@class, "product_main")]/p[contains(@class, "instock")]/text()').extract()[1].strip()
        stars = response.xpath(
            '//div/p[contains(@class, "star-rating")]/@class').extract_first().replace('star-rating ', '')
        description = response.xpath(
            '//div[@id="product_description"]/following-sibling::p/text()').extract_first()
        upc = response.xpath(
            '//table[@class="table table-striped"]/tr[1]/td/text()').extract_first()
        price_excl_tax = response.xpath(
            '//table[@class="table table-striped"]/tr[3]/td/text()').extract_first()
        price_inc_tax = response.xpath(
            '//table[@class="table table-striped"]/tr[4]/td/text()').extract_first()
        tax = response.xpath(
            '//table[@class="table table-striped"]/tr[5]/td/text()').extract_first()

        yield {
            'Title': title,
            'Image': final_image,
            'Price': price,
            'Stock': stock,
            'Stars': stars,
            'Description': description,
            'Upc': upc,
            'Price after tax': price_excl_tax,
            'Price incl tax': price_inc_tax,
            'Tax': tax,
        }
