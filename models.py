"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = 'https://www.personality-insights.com/wp-content/uploads/2017/12/default-profile-pic-e1513291410505.jpg'

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, 
                    primary_key=True)
    first_name = db.Column(db.String(50),
                            nullable=False)
    last_name = db.Column(db.String(50),
                            nullable=False)
    image_url = db.Column(db.String,
                            nullable=False,
                            default='DEFAULT_IMG_URL')
    
    @property
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    
def connect_db(app):
    db.app = app
    db.init_app(app)