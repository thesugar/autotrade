import pandas as pd
import numpy as np
from oandapyV20 import API
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingStream
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import settings
import traceback

accountID = "101-009-13639425-001"

def connect():
    
    access_token = settings.ACCESS_TOKEN
    api = API(access_token=access_token, environment="practice")
    return api

def get_currency_info(currency_pair: str, api: API):

    """
    Get the designated currency pair's information (e.g.minimum tradable unit, split rate, and so on)

    Parameters
    ----------
    currency_pair : str
        currency pair you want to get information
        e.g. "USD_JPY"

    api : API

    Returns
    -------
    r : JSON
        information of currency pair you designated
    """

    if type(currency_pair) != str:
        raise Exception('please set currency pair with String.')

    params = { "instruments" : currency_pair }
    try:
        r = accounts.AccountInstruments(accountID = accountID, params=params)
    except Exception:
        traceback.print_exc()
        print('exception was throwned when app tries to fetch currency info from API.')
    
    return api.request(r)

def get_account_info(api: API):

    """
    Get information about your account
    """

    r = accounts.AccountSummary(accountID)
    return api.request(r)

def get_price_data(currency_pair:str, count: int, granularity: str, api: API):

    """
    Get Price Data

    Parameters
    ----------
    currency_pair : str
        currency pair you want to get information
        e.g. "USD_JPY"
    
    count : int
        the amount of data you want to fetch (maximum: 5000)

    granularity : str
        "S5", "S10", "S15", "S30" (S stands for seconds)
        "M1", "M2", "M4", "M5", "M10", "M15", "M30" (M stands for minutes)
        "H1", "H2", "H3", "H4", "H6", "H12"
        "D"
        "W"
        "M"

    api : API

    Returns
    -------
    r : JSON
        information of price data
    """

    if type(currency_pair) != str:
        raise Exception('please set currency pair with String.')

    if count > 5000:
        raise Exception('parameter `count` must be equal or less than 5000')

    params = { "count" : count, "granularity": granularity }
    try:
        r = instruments.InstrumentsCandles(instrument=currency_pair, params=params)
    except Exception:
        traceback.print_exc()
        print('exception was throwned when app tries to fetch price data from API')
    
    return api.request(r)


if __name__ == '__main__':

    print('start processing')
    api = connect()

    print('口座情報を取得します')
    print(get_account_info(api=api))

    print('通貨ペアの情報を取得します')
    print(get_currency_info(currency_pair="USD_JPY", api=api))

    print('価格情報を取得します')
    print(get_price_data(currency_pair="USD_JPY", count=100, granularity="M5", api=api))

    print('Done!')


