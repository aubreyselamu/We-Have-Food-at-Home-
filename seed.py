from models import User, Favorite, Recipe, db
from app import app

db.drop_all()
db.create_all()

#If User table isn't empty, empty it
User.query.delete()

#Add users
Aubrey = User.signup(username = 'aubrey.selamu', password = 'Ethiopia_1998', email = 'aubrey@gmail.com')
Olani = User.signup(username = 'olani.mendes', password = 'nani174life', email = 'olani@ics.edu')
Yohanna = User.signup(username = 'yohanna123', password = 'cookieswirl', email = 'yohanna@yahoo.com')

#Add new objects to session
db.session.add(Aubrey)
db.session.add(Olani)
db.session.add(Yohanna)

#Commit to session
db.session.commit()

#If Recipe table isn't empty, empty it
Recipe.query.delete()

#Add users
strudel = Recipe(id = 73420, 
                image_url = 'https://spoonacular.com/recipeImages/73420-312x231.jpg', 
                name = 'Apple Or Peach Strudel',
                ingredients = 'apples, egg, cinnamon, baking powder')

apricot = Recipe(id = 632660, 
                image_url = 'https://spoonacular.com/recipeImages/632660-312x231.jpg', 
                name = 'Apricot Glazed Apple Tart',
                ingredients = 'unsalted butter, red apples, cinnamon, apricot reserves')



#Add new objects to session
db.session.add(strudel)
db.session.add(apricot)

#Commit to session
db.session.commit()