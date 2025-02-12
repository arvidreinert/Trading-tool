import read_data as rd
import finance_data as fd
from fisims import sim
import time

class sma_daytrader_bot():
    def __init__(self,stocks_allowed):
        self.chunk = rd.data_chunk()
        self.boughts = {}
        for stock in stocks_allowed:
            self.chunk.add_symbol(stock)
            self.boughts[stock] = 0

    def is_bought(self,stock):
        cond = False
        if stock in self.boughts:
            if self.boughts[stock] > 0:
                cond = True
        return cond
    def refresh_symbol(self,stock):
        fd.create_data(stock,interval="1m",duration={ "days": 5,"hours": 0,"minutes": 0,"seconds": 0 })
        self.chunk.prepare_data(stock)

    def signal(self,stock):
        cp = fd.search_comp(stock)
        self.refresh_symbol(stock)
        sma = self.chunk.sma(stock)
        cls = self.chunk.get_data(stock,"closes")
        gain = cls[-1]-cls[0]
        stre = round(gain/sma*100,2)
        print(stre)
        if cp < sma and stre >= 3:
            return "buy"
        elif cp > sma:
            return "sell"
        if cp == sma:
            return "sell"

bot = sma_daytrader_bot(["AAPL"])
simulator = sim(10)
print(bot.signal("AAPL"))