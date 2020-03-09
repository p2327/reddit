from datetime import datetime as dt 
import scrapy
from reddit.items import RedditItem

# Using the template from Scrapy docs
class PostSpider(scrapy.Spider):
    name = 'post' 
    allowed_domains = ['reddit.com']

    # (sub, time period) 
    reddit_urls = [
        ('Jokes', 'week'),
        ('funny', 'week')
    ]

    # New url lazy loads https://www.reddit.com/r/funny/top/?t=week
    # Old url pagination https://www.reddit.com/r/funny/top/?sort=top&t=week
    start_urls = [
        # 'https://www.reddit.com/r/' + sub + '/top/?t=' + period
        'https://old.reddit.com/r/' + sub + '/top/?sort=top&t=' + period
        for sub, period in reddit_urls
    ]

    def parse(self, response):
        # Get the subreddit from the URL
        sub = response.url.split('/')[4]

        # Parse through each of the posts
        for post in response.css('div.thing'):
            item = RedditItem()

            item['date'] = dt.today()
            item['date_str'] = item['date'].strftime('%Y-%m-%d')
            item['sub'] = sub
            item['title'] = post.css('a.title::text').extract_first()

            item['url'] = post.css('a.title::attr(href)').extract_first()
            # If self-post, add reddit base url (as it's relative by default)
            if item['url'][:3] == '/r/':
                #item['url'] = 'https://www.reddit.com' + item['url']
                item['url'] = 'https://old.reddit.com' + item['url']

            #item['score'] = int(post.css('div.unvoted::text').extract_first())
            #print(post.css('div.unvoted::text').extract_first().strip('k'))
            item['score'] = 1000*float(post.css('div.unvoted::text').extract_first().strip('k'))
            #item['commentsUrl'] = post.css('a.comments::attr(href)').extract_first()
            #print('PRINTERROR' + post.css('a.comments::attr(href)').extract_first())
            item['comments_url'] = post.css('a.comments::attr(href)').extract_first()

            yield item
