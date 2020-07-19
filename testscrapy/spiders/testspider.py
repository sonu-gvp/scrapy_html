# -*- coding: utf-8 -*-
import scrapy
import lxml
from lxml import etree, html
import re
import pandas as pd



class TestspiderSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['hubertiming.com']
    start_urls = ['https://www.hubertiming.com/results/2017GPTR10K']
    def start_requests(self):
        for url in self.start_urls:
            request = scrapy.Request(url=url,callback=self.parse_product,dont_filter=True)
            yield request

    def parse_product(self, response):
        table_details = {}
        response_text = response.text
        hxs = lxml.html.document_fromstring(response_text)
        header_data = hxs.xpath("//tr[contains(@class, 'header')]/th/text()")

        for header in header_data:
            table_details[header] = {}
        print('table_details: ', table_details)
        list_rows = []
        tbody_data = hxs.xpath("//tbody/tr/td/text()")
        for tbody in tbody_data:
            list_rows.append(tbody.replace("\n", "").replace("\r", ""))

        df = pd.DataFrame(list_rows)
        print('df: ', df.head(10))
        # html = etree.tostring(i, encoding='UTF-8', pretty_print=True)
        # print('\n\n\nhtml: ', html)
