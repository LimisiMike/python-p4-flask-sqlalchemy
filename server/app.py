#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
    
    
# After creating our app and models, follow the steps below in the terminal;
    # export FLASK_APP=app.py
    #export FLASK_RUN_PORT=5555
    #flask db init

# In the models.py, under the app.config, Let's heed that warning and set SQLALCHEMY_TRACK_MODIFICATIONS to False. => app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# We can jump straight into migrating:
     #   $flask db revision --autogenerate -m'Create tables owners, pets'
     
#...and pushing those migrations to our database:
        # $flask db upgrade head