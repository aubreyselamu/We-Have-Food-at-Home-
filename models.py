'''SQLAlchemy Models for We Got Food At Home!'''

from flask_sqlalchemy import SQLAlchemy 
db = SQLAlchemy()

def connect_db(app):
    '''Connec this database to provided Flaks app'''

    db.app = app
    db.init_app(app)

class User(db.Model):
    '''User in System'''

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key = True)
    
    username = db.Column(
            db.Text,
            nullable = False,
            unique = True
    )

    password = db.Column(
            db.Text,
            nullable = False,
    )

    email = db.Column(
            db.Text,
            nullable = False,
            unique = True
    )

class Recipe(db.Model):
    '''An individual recipe'''

    __tablename__ = 'recipes'

    id = db.Column(
        db.Integer,
        nullable = False
    )

    image_url = db.Column(
        db.Text,
        nullable = False
    )

    title = db.Column(
        db.Text
    )

    ingredients = db.Column(
        db.Text
    )

class Favorite(db.Model):

    __tablename__ = 'favorites'

    id = db.Column(
        db.Integer,
        primary_key = True,
    )

    user_id = db.Column(
            db.Integer,
            db.ForeignKey('users.id', ondelete = 'cascade')
    )

    recipe_id = db.Column(
            db.Integer,
            db.ForeignKey('recipes.id', ondelete = 'cascade')
    ))

