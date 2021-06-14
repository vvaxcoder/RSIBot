import websocket, json, pprint

# from github https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#general-wss-information
SOCKET = "wss://stream.binance.com:9443/ws/dogeusdt@kline_1m"
closes = []

def on_open_func(ws):
    print('the connection has opened')

def on_close_func(ws):
    print('the connection has closed')

def on_message_func(ws, message):
    global closes

    # print(message)
    json_message = json.loads(message)
    # pprint.pprint(json_message) # see Payload section for more details

    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))

ws = websocket.WebSocketApp(SOCKET, on_open=on_open_func, on_close=on_close_func, on_message=on_message_func)
ws.run_forever()