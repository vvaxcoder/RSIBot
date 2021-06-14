import websocket, json, pprint, talib, numpy

# from github https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#general-wss-information
SOCKET = "wss://stream.binance.com:9443/ws/dogeusdt@kline_1m"
closes = []
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = "DOGEUSD"
TRADE_QUANTITY = 30
in_position = False

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

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all rsis calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Overbought! Sell!")
                    # put binance sell order logic here
                else:
                    print("It is overbought, but we don't own any. Nothing to do.")

            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("It is oversold, but you already own it, nothing to do.")
                else:
                    print("Oversell! Buy!")
                    # put binance buy order logic here

ws = websocket.WebSocketApp(SOCKET, on_open=on_open_func, on_close=on_close_func, on_message=on_message_func)
ws.run_forever()