import websocket

# from github https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#general-wss-information
SOCKET = "wss://stream.binance.com:9443/ws/dogeusdt@kline_1m"

def on_open_func(ws):
    print('the connection has opened')

def on_close_func(ws):
    print('the connection has closed')

def on_message_func(ws, message):
    print('the message has sent')

ws = websocket.WebSocketApp(SOCKET, on_open=on_open_func, on_close=on_close_func, on_message=on_message_func)
ws.run_forever()