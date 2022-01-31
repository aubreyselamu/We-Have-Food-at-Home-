'''SQLAlchemy Models for We Got Food At Home!'''

import bcrypt
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
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

    favorites = db.relationship(
        'Recipe',
        secondary="favorites"
    )

    @classmethod
    def signup(cls, username, password, email):
        '''Sign up user'''

        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf8')

        user = User(
            username = username,
            password = hashed_pwd,
            email = email
        )

        db.session.add(user)
        db.session.commit()
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        '''Find user with `username` and `password`'''

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user
        
        return False

class Recipe(db.Model):
    '''An individual recipe'''

    __tablename__ = 'recipes'

    id = db.Column(
        db.Integer,
        primary_key = True,
        nullable = False
    )

    image_url = db.Column(
        db.Text,
        nullable = False
    )

    name = db.Column(
        db.Text
    )

    favorite_recipes = db.relationship('Favorite', backref = 'recipe')

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
    )

