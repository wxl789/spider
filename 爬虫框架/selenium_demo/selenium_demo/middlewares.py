# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:

from scrapy.http import HtmlResponse


class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        url = request.url
        #self.chrome.get(url)
        #html = self.chrome.page_source
        spider.chrome.get(url)
        html = spider.chrome.page_source
        return HtmlResponse(url=url, body=html, request=request, encoding='utf-8')

