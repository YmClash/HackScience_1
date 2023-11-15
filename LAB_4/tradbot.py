import os
import numpy as np
import talib
from binance.client import Client
from dotenv import load_dotenv
import LAB_1.ymc as ymc
import websocket,json,pprint
from datetime import datetime
import serial
import time
import pyfirmata as firmata

# ymc.method_list(np)


load_dotenv()


board  =  firmata.Arduino("COM3")

print(board)

it = firmata.util.Iterator(board)
it.start()

led = board.get_pin('d:13:o')




SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"


RSI_PERIOD = 14
RSI_OVERBUY = 10
RSI_OVERSELL = 10

fermeture = []


#blink fonction

def blink():
    led.write(1)
    time.sleep(0.001)
    led.write(0)
    led.write(1)
    time.sleep(1)
    led.write(0)




def on_open(ws) :
    print("Open connection ")

def on_close(ws) :
    print("connexion close")

def on_message(ws,message) :
    print("Message recu ")
    led.write(1)
    time.sleep(0.01)
    led.write(0)

    json_message = json.loads(message)
    # pprint.pprint(json_message)

    candle = json_message['k']
    is_candle_close = candle['x']
    close = candle['c']

    open = candle['o']



    if is_candle_close:
        print(f'Ouverture a :{open} : Fermeture a : {close}')
        fermeture.append(float(close))
        blink()

        print(f'Fermeture'
              f'{fermeture}')



    # pprint.pprint(f'ouverture: {candle_open}:.2f '
    #       f'fermeture: {candle_close}:.2f'
    #       f'TIME     : {time}')

ws = websocket.WebSocketApp(SOCKET,on_open=on_open,on_close=on_close,on_message=on_message)


ws.run_forever()



