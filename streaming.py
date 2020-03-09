import oandapyV20
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
import oandapyV20.endpoints.pricing as pricing
from main import connect
import settings
import json

accountID = "101-009-13639425-001"
access_token = settings.ACCESS_TOKEN
api = connect()

params ={ "instruments": "USD_JPY" } # 他の通貨も表示したいときは"USD_JPY,EUR_USD"などとする（カンマの後にスペース不要）
r = pricing.PricingStream(accountID=accountID, params=params)

try:
    for R in api.request(r):
        try:
            print(json.dumps(R["bids"][0]["price"], indent=2)) # 自分が売る価格
            print(json.dumps(R["asks"][0]["price"], indent=2)) # 自分が買う価格
        except KeyError:
            pass

except V20Error as e:
    print("Error: {}".format(e))