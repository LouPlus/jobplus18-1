# _*_ coding : UTF-8 _*_
#开发人员 ： 纠结中的忐忑
#开发时间 ： 2020/6/1  8:08
#文件名称 ： demo.py.PY
#开发工具 ： PyCharm

import scrapy

class JobSpider(scrapy.Spider):
    name = 'job'

    start_url = ['http://120.55.127.115/job/']

    def parse(self, response):
        for job in response.css('div.col-sm-6'):
            yield{

            }