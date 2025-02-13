from bot1 import *

symbols = ["AAPL","GOOG","NVDA","MSFT","META","GAN"]
bot = sma_daytrader_bot(symbols)
simulator = sim(10)
counter = 0
while True:
    if counter == 1000:
        for symbol in symbols:
            sig = bot.signal(symbol)
            print(sig)
            if not sig[0] == None:
                print(simulator.execute_bot(round(abs(sig[1])),symbol,sig[0]))
        counter = 0
    counter += 1