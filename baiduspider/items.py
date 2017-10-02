# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionItem(scrapy.Item):

    questionNum = scrapy.Field()
    question = scrapy.Field()
    questionDes = scrapy.Field()
    questionUrl = scrapy.Field()

class BestansItem(scrapy.Item):
    questionNum = scrapy.Field()

    bestAns = scrapy.Field()
    bestPostime = scrapy.Field()
    bestAuthor = scrapy.Field()
    bestUp = scrapy.Field()
    bestDown = scrapy.Field()
    rate = scrapy.Field()

class OtheransItem(scrapy.Item):
    questionNum = scrapy.Field()

    otherAns = scrapy.Field()
    otherPostime = scrapy.Field()
    otherAuthor = scrapy.Field()
    otherUp = scrapy.Field()
    otherDown = scrapy.Field()
    rate = scrapy.Field()


