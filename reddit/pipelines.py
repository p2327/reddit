import logging
import pymongo
from reddit.items import RedditItem
import scrapy


"""
Once an item is scraped by the spider,
process it through a pipeline to:

    - cleanse HTML data
    - validate scraped data (checking that the items contain certain fields)
    - check for duplicates (and dropping them)
    - store the scraped item in a database

"""
# No pre-processing required 
# Setup MongoDB to store the data


class MongoPipeline(object):

    collection_name = 'top_reddit_posts'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        """ 
        Creates a pipeline instance from a Crawler object.
        The Crawler object provides access to settings; 
        it is how the pipeline access them and hook 
        its functionality into Scrapy.
        """
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )
    
    def open_spider(self, spider):
        """ 
        Initialise spider and open db connection.
        """
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        """
        Clean up when spider is closed
        """
        self.client.close()

    def process_item(self, item: RedditItem, spider: scrapy.Spider) -> dict:
        """
        Post handling.
        Returns a dict with data.
        """
        self.db[self.collection_name].insert(dict(item))
        logging.debug("Post added to MongoDB")
        return item


