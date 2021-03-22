# -*- coding: utf-8 -*-
import scrapy


class LegoProductsSpider(scrapy.Spider):
    name = 'lego_products'
    allowed_domains = ['lego.com']
    start_urls = ['https://www.lego.com/en-us/categories/new-sets-and-products']

    def parse(self, response):
        categories = response.xpath('//*[@class="cat-list"]/li')
        for category in categories:
            url = category.xpath('.//*[@class="cat-list__see-products"]/@href').extract_first()
            absolute_url = response.urljoin(url)
            yield scrapy.Request(absolute_url,
                                 callback=self.parse_category,
                                 dont_filter=True)

    def parse_category(self, response):
        products = response.xpath('.//*[@class="product-leaf__link-title"]/@href').extract()
        for product in products:
            absolute_url = response.urljoin(product)
            yield scrapy.Request(absolute_url,
                                 callback=self.parse_product)

        # More product?
        show_all = response.xpath('.//*[@class="pagination__view-all"]/@href').extract_first()
        if show_all:
            absolute_url = response.urljoin(show_all)
            yield scrapy.Request(absolute_url,
                                 callback=self.parse_category)

    def parse_product(self, response):
        name = response.xpath('//*[@class="overview__name markup"]/text()').extract_first()
        price = response.xpath('//*[@class="product-price__list-price"]/text()').extract_first()
        available = response.xpath('//*[@class="available--now"]/text()').extract_first()
        description = response.xpath('//*[@class="product-details__description markup"]/text()').extract_first()
        code = response.xpath('//*[@class="product-details__product-code"]/text()').extract_first()
        vip_points = response.xpath('//*[@class="product-details__vip-points"]/text()').extract_first()
        ages = response.xpath('//*[@class="product-details__ages"]/text()').extract_first()
        pieces = response.xpath('//*[@class="product-details__piece-count"]/text()').extract_first()
        featured = response.xpath('//*[@class="badges__flag"]/text()').extract_first()
        category = response.xpath('//*[@class="badges__tag"]/text()').extract_first()
        if name:
            yield {'Name': name,
                   'Price': price,
                   'Availability': available,
                   'Description': description,
                   'Code': code,
                   'vip_points': vip_points,
                   'Ages': ages,
                   'Pieces': pieces,
                   'Featured': featured,
                   'Category': category}
