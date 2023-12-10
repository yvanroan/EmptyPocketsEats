from os import environ
from dotenv import load_dotenv

load_dotenv()

# class Config():
SPOON_API_KEY = environ.get('SPOON_API_KEY')
EDAM_API_KEY = environ.get('EDAM_API_KEY')
EDAM_API_ID = environ.get('EDAM_API_ID')
    
# Add other configuration variables as needed

# class DevelopmentConfig(Config):
#     DEBUG = True
#     # Development specific configurations

# class ProductionConfig(Config):
#     DEBUG = False
#     # Production specific configurations

