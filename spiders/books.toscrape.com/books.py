import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    base_url = 'http://books.toscrape.com'

    def parse(self, response):

        all_books = response.css('article.product_pod')

        for book in all_books:
            # title = book.css('h3 a::attr(title)').extract_first()
            # price = book.css('div p.price_color::text').extract_first()

            # get to the detailed book URL
            # image_url = self.start_urls[0] + book.css('img.thumbnail::attr(src)').extract_first()
            book_url = self.start_urls[0] + book.css('h3 a::attr(href)').extract_first()

            # follow link book_url and run function parse_book
            yield scrapy.Request(book_url, callback=self.parse_book)

            # yield {
            #     'first_page_title': title,
            #     'first_page_price': price,
            #     'first_page_Image URL': image_url,
            #     'first_page_Book URL': book_url,
            # }

    def parse_book(self, response):
        # check if is working
        # print(response.status)
        title = response.css('div h1::text').extract_first()
        # check if is working
        # print(title)

        relative_image = response.css(
            'div.item.active img::attr(src)').extract_first()
        
        ##generate full link
        final_image = self.base_url + relative_image.replace('../..', '')
        
        ## remove £
        price = response.css('div .product_main p.price_color::text').extract_first().replace('£', '')
        
        ## remove <i class="icon"></i>
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
            'Price excl tax': price_excl_tax,
            'Price incl tax': price_inc_tax,
            'Tax': tax,
        }
