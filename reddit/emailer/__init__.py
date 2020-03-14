from mongoengine.connection import connect
from .data_model import Post
from .render_template import render
from .mailgun_emailer import send_email


def email_last_scraped_date():
    # Connect to db
    MONGO_URI = 'mongodb+srv://pete:d71RZ9Xu46NkPxL7@paws-sandbox-gdqa2.mongodb.net/paws-sandbox?ssl=true&ssl_cert_reqs=CERT_NONE'
    connect('paws-sandbox', host=MONGO_URI)

    # Get the last date the webscraper was run by loading the latest post added
    for post in Post.objects().fields(date_str=1).order_by('-date_str').limit(1):
        day_to_pull = post.date_str

    # Pass in variables, render template, and send
    context = {
        'day_to_pull': day_to_pull,
        'Post': Post,
    }
    html = render("template.html", context)
    send_email(html)