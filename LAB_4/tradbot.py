import ccxt
import os
import pandas as kuma
import matplotlib.pyplot as ploti
import numpy as np
import talib
from binance.client import Client
from dotenv import load_dotenv
import LAB_1.ymc as ymc
import websocket

# ymc.method_list(np)


SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"


def on_open() :
    print("Open connection ")


def on_close() :
    print("connexion close")


def on_message(ws,message) :
    print("Message recu ",message)

ws = websocket.WebSocketApp(SOCKET,on_open=on_open,on_close=on_close,on_message=on_message)
ws.run_forever()



