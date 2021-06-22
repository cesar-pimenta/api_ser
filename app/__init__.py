from flask_restful import Api
from flask import Flask
from flask_caching import Cache
from config import config
from app.resources.stock import Stock

cache = Cache()


def create_app(config_name):
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = 'simple'
    app.config.from_object(config[config_name])
    cache.init_app(app)
    api = Api(app, prefix="/serasa")

    api.add_resource(Stock, "/stock")

    return app 
