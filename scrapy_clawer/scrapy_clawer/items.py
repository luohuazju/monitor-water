# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import TakeFirst, MapCompose

class WaterItem(scrapy.Item):
    releaseDate = scrapy.Field(output_processor=TakeFirst())
    releaseString = scrapy.Field(output_processor=TakeFirst())