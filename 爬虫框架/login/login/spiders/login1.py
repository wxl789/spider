# -*- coding: utf-8 -*-
import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['sxt.cn']

    # start_urls = ['http://www.sxt.cn/index/login/login.html']
    def start_requests(self):
        url = 'http://www.sxt.cn/index/login/login.html'
        form_data = {
            "user": "17703181473",
            "password": "123456"
        }
        yield scrapy.FormRequest(url,formdata=form_data,callback=self.parse)
    def parse(self, response):
       # print(response.text)
        yield scrapy.Request('http://www.sxt.cn/index/user.html',callback=self.parse_info)
    def parse_info(self,response):
        print(response.text)