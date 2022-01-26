# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


"""
Custom function that can be mentioned within the MapCompose input_processor
"""
def do_something(value):
    result = value.replace("foo", "").strip()
    return result

"""
Define here what should happen to each scraped value
"""
class YourSpiderItem(scrapy.Item):
    # add all of your scraped values here (for this example, we have only two)
    name = scrapy.Field(input_processor=MapCompose(remove_tags, do_something),
                        output_processor=TakeFirst())
    year = scrapy.Field()
