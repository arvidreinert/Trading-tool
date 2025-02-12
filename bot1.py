import read_data as rd
import finance_data as fd
from fisims import sim

class sma_bot():
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

    def signal(self,stock,bought=False):
        sma = self.chunk

bot = sma_bot(["AAPL"])
simulator = sim(10)
bot.signal()