from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User():
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    usernmae = db.Column(db.String(32), unique=True, index=True, nullable=False)
    