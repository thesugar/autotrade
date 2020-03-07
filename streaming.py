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

params ={ "instruments": "USD_JPY" }
r = pricing.PricingStream(accountID=accountID, params=params)
print(r)

MAXREC = 10

try:
    for R in api.request(r):
        try:
            print(json.dumps(R["bids"][0]["price"], indent=2))
        except KeyError:
            pass

except V20Error as e:
    print("Error: {}".format(e))