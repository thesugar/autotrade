import pandas as pd
import numpy as np
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import settings

def connect():
    
    access_token = settings.ACCESS_TOKEN
    api = API(access_token=access_token, environment="practice")
    return api

if __name__ == '__main__':

    accountID = "101-009-13639425-001"

    print('start processing')
    api = connect()

    params = { "count" : 10, "granularity": "W" }
    r = instruments.InstrumentsCandles(instrument="USD_JPY", params=params)
    chart_data = pd.DataFrame(api.request(r)['candles'])
    chart_data['time'] = chart_data['time'].apply(lambda x: x[:9])
    print(chart_data)


