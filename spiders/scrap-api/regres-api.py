# -*- coding: utf-8 -*-
import scrapy
import json


class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['reqres.in']
    start_urls = ['https://reqres.in/api/users?page=1']

    def parse(self, response):
        # get api full request
        # print(response.body)
        resp = json.loads(response.body)
        quotes = resp.get('data')
        for quote in quotes:
            yield {
                'email': quote.get('email'),
                'first_name': quote.get('first_name'),
                'avatar': quote.get('avatar')
            }
        #ref has_next: true
        #has_next = resp.get('per_page')
        #if has_next:
            #incrementa + 1 na ref page: 1
            next_page = resp.get('page') + 1
            yield scrapy.Request(
                url=f'https://reqres.in/api/users?page={next_page}',
                callback=self.parse
            )
