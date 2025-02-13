from bot1 import *
import time

symbols = ["GOOG"]
bot = sma_daytrader_bot(symbols)
simulator = sim(10)
counter = 0
start_time = time.perf_counter()
try:
    while True:
        time.sleep(5)
        for symboll in symbols:
            time.sleep(1)
            sig = bot.signal(symboll)
            if len(sig) >= 5:
                print(f"{symboll}:{sig[0]},price:{sig[1]},gain/loss:{sig[3]} or {round(float(sig[3])/float(sig[1]),4)}%")
            if sig[0] == "buy":
                print(simulator.execute_bot(1,symboll,sig[0]))
            if sig[0] == "sell":
                print(simulator.execute_bot(simulator.stocks[symboll]["longs"],symboll,"sell"))
                break
except:
    end_time = time.perf_counter()
    print(f"stopped after {end_time - start_time} seconds. Thats {(end_time - start_time)/60} minutes")
    simulator.portfolio()