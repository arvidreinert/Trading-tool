import read_data as rd
import finance_data as fd
from fisims import sim

class sma_bot():
    def __init__(self,stocks):
        self.chunk = rd.data_chunk()
        self.boughts = {}
        for stock in stocks:
            self.chunk.add_symbol(stock)
            self.boughts[stock] = 0

    def signal(bought=False):
        pass

bot = sma_bot(["AAPL"])
simulator = sim(10)
bot.signal()