from bot1 import *

symbols = ["AAPL","GOOG","NVDA","MSFT","META"]
bot = sma_daytrader_bot([symbols])
simulator = sim(10)
counter = 0
while True:
    if counter == 120:
        for symbol in symbols:
            sig = bot.signal(symbol)
            print(sig)
            print(simulator.execute_bot(round(sig[1]),symbol,sig[0]))
        counter = 0
    counter += 1