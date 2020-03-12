from mongoengine.document import Document
from mongoengine.fields import DateTimeField, IntField, StringField, URLField


class Post(Document):
    """
    Defines structure of reddit_top_posts collection.
    """
    comments_url = URLField(required=True)
    date = DateTimeField(required=True)
    date_str = StringField(max_length=10, required=True)
    score = IntField(required=True)
    sub = StringField(max_length=20, required=True)
    title = StringField(max_lenght=300, required=True)
    url = URLField(required=True)

    meta = {
        'collection': 'top_reddit_posts',
        'ordering': ['-score'],
        'auto_create_index': False
    }