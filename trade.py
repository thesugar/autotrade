import oandapyV20.endpoints.orders as orders
from main import connect
import traceback
import settings

accountID = "101-009-13639425-001"
access_token = settings.ACCESS_TOKEN
api = connect()

def make_order(kind: str, units: int, order_type: str):

    if kind not in ["buy", "sell"]:
        raise Exception('kind must be "buy" or "sell"')

    if order_type not in ["MARKET", "STOP", "LIMIT"]:
        raise Exception('order_type must be "MARKET", "STOP" or "LIMIT"\
            \n"MARKET"...成行\
            \n"STOP"...逆指値\
            \n"LIMIT"...指値')

    if kind == 'buy':
        units = "+" + str(units)
    
    if kind == 'sell':
        units = "-" + str(units)

    order_data = {
            "order": {
            "instrument": "USD_JPY",
                "units": units,
                "type": order_type,
            }
        }

    try:
        o = orders.OrderCreate(accountID, data=order_data)
        api.request(o)
        return o.response
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    result = make_order(kind='buy', units=10, order_type='MARKET')
    print(result)