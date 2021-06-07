from config import FlaskConfig
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_migrate import Migrate
# from flask_cors import CORS
# from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(FlaskConfig)

# db = SQLAlchemy(app)
# ma = Marshmallow(app)
# migrate = Migrate(app, db)
# CORS(app)
# mail = Mail(app)
