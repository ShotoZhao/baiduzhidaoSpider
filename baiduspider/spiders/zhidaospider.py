# -*- coding: utf-8 -*-
import scrapy
from baiduspider import items
import re
import random

class ZhidaospiderSpider(scrapy.Spider):
    name = 'zhidaospider'
    allowed_domains = ['zhidao.baidu.com']
    start_urls = ['https://zhidao.baidu.com/question/325952789.html']

    def parse(self, response):
        try:
            questionnumpat = re.compile(r'question/(\d+).html')
            item = items.QuestionItem()
            itemother = items.OtheransItem()
            itembest = items.BestansItem()

            item['question'] = response.xpath('//head/title/text()').extract()[0]
            item['questionDes'] = response.xpath('//article[@class="grid qb-content"]//div[contains(@class,"q-content")]//span[@class="con"]/text()').extract()
            item['questionUrl'] = response.url
            item['questionNum'] = questionnumpat.findall(response.url)[0]
            yield item
        except Exception,e:
            print e

        nodes = response.xpath('//div[@id="wgt-answers"]//div[contains(@class,"line content")]')

        for node in nodes:
            try:
                if node.xpath('.//div[@class="long-question"]/text()'):
                    itemother['otherAns'] = node.xpath('.//div[@class="long-question"]/text()').extract()
                else:
                    itemother['otherAns'] = node.xpath('.//span[@class="con"]/text()').extract()
                itemother['questionNum'] = questionnumpat.findall(response.url)[0]
                itemother['otherPostime'] = node.xpath('.//span[contains(@class,"pos-time")]/text()').extract()[0]
                itemother['otherAuthor'] = node.xpath('.//a[@class="user-name"]/text()').extract()
                itemother['otherUp'] = int(node.xpath('.//div[@class="qb-zan-eva"]/span/@data-evaluate')[0].extract())
                # a = pat.findall(response.body)
                # itemother['otherUp']= ','.join(a)
                itemother['otherDown'] = int(node.xpath('.//div[@class="qb-zan-eva"]/span/@data-evaluate')[1].extract())
                print '--------------------------------'
                print itemother['otherUp']
                print itemother['otherDown']
                itemother['rate'] = float(itemother['otherUp'])/(float(itemother['otherDown']) + 0.5)
                if itemother['rate'] > 3:
                    yield itemother
            except Exception,e:
                print e


        if response.xpath('//article[@class="grid qb-content"]//div[contains(@class,"wgt-best")]//pre/text()'):
            try:
                itembest['questionNum'] = questionnumpat.findall(response.url)[0]
                itembest['bestAns'] =response.xpath('//article[@class="grid qb-content"]//div[contains(@class,"wgt-best")]//pre/text()').extract()
                itembest['bestUp'] = int(response.xpath('//article[@class="grid qb-content"]//div[contains(@class,"wgt-best")]//div[@class="qb-zan-eva"]/span/@data-evaluate')[0].extract())
                itembest['bestDown'] = int(response.xpath('//article[@class="grid qb-content"]//div[contains(@class,"wgt-best")]//div[@class="qb-zan-eva"]/span/@data-evaluate')[1].extract())
                itembest['bestPostime'] = response.xpath('//article[@class="grid qb-content"]//div[contains(@class,"wgt-best")]//span[contains(@class,"pos-time")]/text()').extract()
                itembest['bestAuthor'] = response.xpath('//article[@class="grid qb-content"]//div[contains(@class,"wgt-best")]//a[@class="user-name"]/text()').extract()
                itembest['rate'] = float(itembest['bestUp'])/(float(itembest['bestDown']) + 1.01)
                if itembest['rate']>3:
                    yield itembest

            except Exception,e:
                print e

        linklist = response.xpath('//article[@class="grid qb-content"]//li/a/@href').extract()
        for link in linklist:
            head = 'https://zhidao.baidu.com'
            yield scrapy.Request(head+link, callback=self.parse)
