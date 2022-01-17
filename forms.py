from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class UserAddForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    email = StringField('E-mail', validators=[DataRequired(), Email()])

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

class IngredientForm(FlaskForm):
    '''Form for adding ingredients to yield recipes'''

    ingredients = StringField('apples, brocolli, fish, garlic')
