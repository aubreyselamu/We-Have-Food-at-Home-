import os
import requests

from flask import Flask, render_template, request, redirect, session, flash, g
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Recipe, Favorite
from forms import IngredientForm, UserAddForm, LoginForm
from sqlalchemy.exc import IntegrityError

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///fridge'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")


connect_db(app)
db.create_all()

##############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    
    else:
        g.user = None

def do_login(user):
    '''Log in user.'''

    session[CURR_USER_KEY] = user.id

def do_logout():
    '''Logout user.'''

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

@app.route('/signup', methods = ["GET", "POST"])
def signup():

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                    username = form.username.data,
                    password = form.password.data,
                    email = form.email.data
                )
        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('user/signup.html', form=form)

        do_login(user)

        return redirect('/')
    else:
        return render_template('user/signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('user/login.html', form=form)

@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    flash("You have successfully logged out", 'success')
    return redirect('/login')

@app.route('/')
def test():
    return render_template('base.html')

##############################################################################
# Recipe Routes

@app.route('/search')
def ingredients_search():
    '''Display ingredients form and allow users to enter household ingredients'''
    
    form = IngredientForm()
    return render_template('recipe/search.html', form=form)

@app.route('/recipes', methods = ['POST'])
def get_recipe_list():
    '''Process ingredient form and display a list of recipes to users'''

    form = IngredientForm()

    if form.validate_on_submit():
        ingredients = form.ingredients.data

        res = requests.get('https://api.spoonacular.com/recipes/findByIngredients', 
                params={'apiKey': 'd0a6169003194a3c865ffb59e9373166', 'ingredients': ingredients})
        data = res.json()

        return render_template('hello.html', ingredients=ingredients, data=data)
    else:
        return redirect('/search')





