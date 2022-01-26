# Imports
import scrapy
from items import YourSpiderItem
from scrapy.loader import ItemLoader


"""
Example spider that scrapes information from a root page (that returns json) with main objects
Each main object has a detail page (that returns html), which must be scraped in addition
Scenario: One request to root page and 1-n requests for each detail page
"""
class YourSpider(scrapy.Spider):
    # define basic settings
    name = "yourspider"
    # your root page, must be contained in a list
    start_urls = ["https://www.url.com/"]

    """
    Parse root page (start_urls) containing the main objects (e.g., search result page with books)
    """
    def parse(self, response):
        # iterate through main objects
        for main_object in response.json()["root_element"]:
            # create dictionary that holds information coming from root page (needed for second request)
            item = dict()
            # scrape information (as well as the detail page url) from root page of current main object
            item["name"] = main_object["book_name"]
            # construct url of detail page
            detail_page_url = "https://www.url.com/" + main_object["book_url"]
            # request previously scraped url that contains further detail information about current main object
            # populate item as metadata for the second request
            request = scrapy.Request(detail_page_url,
                                     callback=self.parse_detail_page,
                                     meta={"item": item},
                                     dont_filter=True)
            yield request

    """
    Parse detail page of the current main object (e.g., detail page of a book)
    """
    def parse_detail_page(self, response):
        # read item from response meta data containing information scraped from root page
        item = response.meta["item"]
        # Define the item loader and choose the reponse as selector
        item_loader = ItemLoader(item=YourSpiderItem(), selector=response)
        # populate item loader with all values coming from item dictionary (here we have only one)
        item_loader.add_value("name", item["name"])
        # populate item loader with scraped information coming form detail page (here we have only one)
        item_loader.add_xpath("year", "//span[contains(@class,'book_year')]")
        yield item_loader.load_item()
