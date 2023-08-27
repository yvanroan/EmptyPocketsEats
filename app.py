from flask import Flask, render_template, request
import requests
from urllib.parse import unquote

STATIC_FOLDER = 'templates/assets'

app = Flask(__name__,
            static_folder=STATIC_FOLDER)

API_Key = 'e98ecc3a72ed4311a9179e2263414a06'

@app.route('/home', methods=['GET'])

def home():
    # render the main page with empty recipe list and search query for ingredients and 
    # we will add an option to enter the amount of calories we dont want to go above
    return render_template('home.html', dishes=[], search_query='')

@app.route('/', methods=['GET', 'POST']) # main route for the app

def index():
    if request.method == 'POST': # if a form is submitted
        query = request.form.get('search_query')

        dishes = search_dishes(query) # searhc for recipes/dishes with the ingredient given in the query

        return render_template('debut.html', dishes=dishes, search_query=query)
        #render the page with the search result,
        # hopefully we can still see the query and change it there

    # if it's a get request or no form submitted
    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)

    dishes =  search_dishes(decoded_search_query)

    return render_template('debut.html', dishes = dishes, search_query= decoded_search_query)

def search_dishes(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params ={
        'apiKey': API_Key,
        'query' : query,
        'number' : 5,
        'instrucitonRequired' : True,
        'addRecipeInformation' : True,
        'addRecipeNutrition' : True,
        'fillIngredients' : True,

    }

    response = requests.get(url, params= params)

    if response.status_code == 200:
        data = response.json()

        return data['results']
    return []# since it did not work

@app.route('/recipe/<int:recipe_id>')

def view_recipe(recipe_id):
    search_query = request.args.get('search_query', '')

    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    
    params ={
        'apiKey': API_Key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        dish = response.json()
        return render_template('dish.html', dish=dish, search_query=search_query)
    
    return "It's not you, it's us (ㅠ﹏ㅠ)\n Recipe not Found", 404

if __name__ == '__main__':
    app.run(debug=True)