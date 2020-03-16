"""
Script to crawl posts and store results in MongoDB
"""
import logging
from datetime import date
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from reddit.spiders.post import PostSpider
from reddit.emailer import email_last_scraped_date


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Run on Sundays
    # %A is full weekday name
    if date.strftime(date.today(), '%A').lower() == 'sunday':
        process = CrawlerProcess(get_project_settings())
        process.crawl(PostSpider)
        process.start()
        email_last_scraped_date()
        logger.info('Scrape completed and email sent')
    else:
        logger.info('Script did not run.')
