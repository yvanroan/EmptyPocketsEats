from os import environ
from dotenv import load_dotenv

load_dotenv()

# class Config():
SPOON_API_KEY = environ.get('SPOON_API_KEY')
    
# Add other configuration variables as needed

# class DevelopmentConfig(Config):
#     DEBUG = True
#     # Development specific configurations

# class ProductionConfig(Config):
#     DEBUG = False
#     # Production specific configurations

