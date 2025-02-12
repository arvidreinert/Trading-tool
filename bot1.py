import read_data as rd
import finance_data as fd
from fisims import sim

chunk = rd.data_chunk()
simulator = sim(10)
class sma_bot():
    def __init__(self,stocks):
        self.boughts = {}
        for stock in stocks:
            self.boughts[stock] = 0

    def signal(bought=False):
        fd.create_data("AAPL",save_as_file=True)
        chunk.add_symbol("AAPL")
        chunk.save_data("AAPL")
        sma = chunk.sma("AAPL")
        chunk.max_volume("AAPL")

bot = sma_bot(["AAPL"])
bot.signal()