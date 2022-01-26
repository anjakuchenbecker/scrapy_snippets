# Scrapy Examples & Snippets
Some examples and snippets for usage of the scrapy library (Scrapy is a free and open-source web-crawling framework written in Python)

## folder scrape_root_page_and_related_detail_pages

Example spider that scrapes information from a root page (that returns json) with main objects. Each main object has a detail page (that returns html), which must be scraped in addition. The url of each detail page is contained within the root page.

Scenario: One request to root page and 1-n requests for each detail page.

```yourspider.py``` must be added into the ```spiders``` folder of your scrapy project.

```items.py``` is a file that is auto-generated when using the ```scrapy startproject {yourprojectname}``` command. Copy the example code into that file.

Check out the Scrapy Tutorial for more information regarding default directory structure: https://docs.scrapy.org/en/latest/intro/tutorial.html
