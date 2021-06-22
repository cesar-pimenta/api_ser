from flask_restful import Resource
from time import sleep
from app import request
from . import scrapper


class Stock(Resource):
    def get(self):
        payload = request.only(['region'])
        nav = scrapper.ChromeAuto()
        if payload["region"]:
            nav.site_url('https://finance.yahoo.com/screener/new')
            result = nav.search(payload["region"])
            nav.quit()
            sleep(5)
            return result
        else:
            nav.site_url('https://finance.yahoo.com/screener/new')
            result = nav.default()
            nav.quit()
            sleep(5)
            return result
