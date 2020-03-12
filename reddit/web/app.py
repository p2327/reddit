from flask import Flask, render_template
from models import db, Post


MONGO_URI = 'mongodb+srv://pete:d71RZ9Xu46NkPxL7@paws-sandbox-gdqa2.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE'


# Initialize app instance
# Central registry to view funcs, URL rules
# and template configs
app = Flask(__name__)


app.config['MONGODB_HOST'] = MONGO_URI
app.debug = True

# Initialise app with database
db.init_app(app)


# Routing

