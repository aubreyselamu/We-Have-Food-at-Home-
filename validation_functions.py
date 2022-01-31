def read():
    file = open("ingredients.csv", "r")
    ingredients = [line.strip() for line in file]
    file.close
    return ingredients

def check_valid_ingredient(ingredient):
    ingredient_exists = ingredient in read()

    if ingredient_exists:
        result = True
    else:
        result = False
    
    return result
    



