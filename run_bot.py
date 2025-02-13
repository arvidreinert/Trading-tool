from bot1 import *
import time

symbols = ["SIE.DE","UBSG.SW"]
bot = sma_daytrader_bot(symbols)
simulator = sim(10)
counter = 0
start_time = time.perf_counter()
try:
    while True:
        time.sleep(5)
        for symbol in symbols:
            time.sleep(1)
            sig = bot.signal(symbol)
            print(sig)
            if not sig[0] == None:
                print(simulator.execute_bot(round(abs(sig[1])),symbol,sig[0]))
            if sig[0] == "sell":
                break
except:
    end_time = time.perf_counter()
    print(f"stopped after {end_time - start_time} seconds. Thats {(end_time - start_time)/60} minutes")