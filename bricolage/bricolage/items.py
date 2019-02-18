# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class VeloItem(Item):
    url = Field()
    crawl_date = Field()
    title = Field()
    image_url = Field()
    price = Field()
    description = Field()
