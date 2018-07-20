# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst


class GermanhospitalsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    state_url = Field(output_processor=TakeFirst())
    pass
