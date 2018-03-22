# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy.http import HtmlResponse
from selenium import webdriver

class ChromeHeadlessMiddleware(object):
    def process_request(self, request, spider):
        options = webdriver.ChromeOptions()
        # options.binary_location = '/usr/bin/google-chrome-unstable'
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        browser = webdriver.Chrome(chrome_options=options)
        browser.get(request.url)
        body = browser.page_source
        return HtmlResponse(browser.current_url, body=body, encoding='utf-8', request=request)