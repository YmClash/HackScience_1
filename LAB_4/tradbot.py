import os
import numpy as np
import talib
from binance.client import Client
from dotenv import load_dotenv
import LAB_1.ymc as ymc
import websocket,json,pprint
from datetime import datetime


# ymc.method_list(np)


SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"


RSI_PERIOD = 14
RSI_OVERBUY =
RSI_OVERSELL

fermeture = []
def on_open(ws) :
    print("Open connection ")

def on_close(ws) :
    print("connexion close")

def on_message(ws,message) :
    print("Message recu ")
    json_message = json.loads(message)
    # pprint.pprint(json_message)

    candle = json_message['k']
    is_candle_close = candle['x']
    close = candle['c']

    open = candle['o']



    if is_candle_close:
        print(f'Ouverture a :{open} : Fermeture a : {close}')
        fermeture.append(close)
        print(f'Fermeture'
              f'{fermeture}')



    # pprint.pprint(f'ouverture: {candle_open}:.2f '
    #       f'fermeture: {candle_close}:.2f'
    #       f'TIME     : {time}')

ws = websocket.WebSocketApp(SOCKET,on_open=on_open,on_close=on_close,on_message=on_message)


ws.run_forever()



