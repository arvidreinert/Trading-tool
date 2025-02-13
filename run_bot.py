from bot1 import *

symbol = input("what do you want to trade?")
bot = sma_daytrader_bot([symbol])
simulator = sim(10)
counter = 0
while True:
    if counter == 120:
        sig = bot.signal(symbol)
        print(sig)
        counter = 0
        x = input("DO IT(Y("")/N) or c to stop simulation")
        if x == "" or x.capitalize() == "Y":
            simulator.execute_bot(round(sig[1]),symbol,sig[0])
        if x.lower() == "c":
            break
    counter += 1