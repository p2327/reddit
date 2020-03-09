import scrapy


class RedditItem(scrapy.Item):
    """
    Storage container for the data
    we plan to scrape
    """
    date = scrapy.Field()
    date_str = scrapy.Field()
    sub = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    comments_url = scrapy.Field()
