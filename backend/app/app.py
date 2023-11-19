from flask import Flask,request,jsonify
import requests
from urllib.parse import unquote 
from os import environ
from flask_cors import CORS



# Access environment variables
# API_KEY = os.getenv('API_KEY')
# require('dotenv').config()



app = Flask(__name__)
app.config.from_pyfile('config.py')

API_Key = app.config.get('SPOON_API_KEY')
CORS(app)

@app.route('/api/recipes', methods=['GET'])
def get_dishes():

    search_query = request.args.get('search_query', '')
    query = unquote(search_query)

    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params ={
        'apiKey': API_Key,
        'query' : query,
        'number' : 18,
        'instructionRequired' : True,
        'addRecipeInformation' : True,
        'addRecipeNutrition' : True,
        'fillIngredients' : True,

    }

    response = requests.get(url, params= params)
    
    if response.status_code == 200:
        data = response.json()

        return data['results']
    
    # print(response,API_Key)
    return []# since it did not work

@app.route('/recipe/<int:recipe_id>', methods=['GET'])

def view_recipe(recipe_id):
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    
    params ={
        'apiKey': API_Key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        return response.json()
    
    return jsonify({"error":"It's not you, it's us (ㅠ﹏ㅠ)\n Recipe not Found"}), 404

# @app.errorhandler(404)
# def not_found(error):
#     return "It's not you, it's us (ㅠ﹏ㅠ)\n Recipe not Found", 404


@app.errorhandler(404)

def not_found(error):
    return {'error': 'Not found'}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)