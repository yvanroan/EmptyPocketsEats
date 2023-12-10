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

S_API_Key = app.config.get('SPOON_API_KEY')
app_id = app.config.get('EDAM_API_ID')
app_key = app.config.get('EDAM_API_KEY')
CORS(app)

@app.route('/api/recipes', methods=['GET'])
def get_dishes():

    search_query = request.args.get('search_query', '')
    query = unquote(search_query)

    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params ={
        'apiKey': S_API_Key,
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
        'apiKey': S_API_Key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:

        return response.json()
    
    return jsonify({"error":"It's not you, it's us (ㅠ﹏ㅠ)\n Recipe not Found"}), 404

# @app.errorhandler(404)
# def not_found(error):
#     return "It's not you, it's us (ㅠ﹏ㅠ)\n Recipe not Found", 404

@app.route('/search', methods=['GET'])

def fetch_recipes():
    
    search_query = request.args.get('query', '')
    print(search_query)
    ingredients = unquote(search_query)

    api_url = f'https://api.edamam.com/api/recipes/v2'
    # print(search_query, "yo")
    params = {
        'type' : 'public',
        'q': ingredients,
        'app_id': app_id,
        'app_key': app_key,
        'fields' :["uri","label",'image','source','url','shareAs','ingredientLines','cuisineType','dietLabels'],
        'random' : True,
        'beta' : True

    }
    response = requests.get(api_url, params=params)
    # print(response.json())
    if response.status_code == 200:
        data = response.json()
        
        
        ans = []
        for hit in data['hits']:
            result = {}
            result['key'] = hit['recipe']['uri']
            result['title'] = hit['recipe']['label']
            result['image'] = hit['recipe']['image']
            result['source'] = hit['recipe']['source']
            result['url'] = hit['recipe']['url']
            result['diet'] = hit['recipe']['dietLabels']
            print(result)
            ans.append(result)



        return ans
    
    return jsonify({"error":"It's not you, it's us (ㅠ﹏ㅠ)\n Recipe not Found"}), 404


#nnnnnnnnnnnnnnnnnnnnnnn
@app.errorhandler(404)

def not_found(error):
    return {'error': 'Not found'}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)