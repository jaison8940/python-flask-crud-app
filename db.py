from flask_sqlalchemy import SQLAlchemy
import secrets
from flaskapp import app
import psycopg2

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{secrets.username}:{secrets.password}@{secrets.hostname}/{secrets.dbname}"
db = SQLAlchemy(app)

