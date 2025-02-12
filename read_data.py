import csv
import finance_data

class data_chunk():
    def __init__(self):
        self.symbols = {}
        self.prices = []
        self.closes = []
        self.highs = []
        self.lows = []
        self.opens = []
        self.volumes = []
        self.datetimes =[]

    def add_symbol(self,symbol):
        self.symbols[symbol] = {"datetimes":[], 'closes':[], 'highs':[], 'lows':[], 'opens':[], 'volumes':[]}

    def save_data(self,symbol):
        with open(f"historic_data_{symbol}.csv", mode ='r')as file:
            content = csv.reader(file)
            x = 0
            row = []
            for line in content:
                if x == 0:
                    row = line
                else:
                    self.symbols[symbol]["datetimes"].append(line[0])
                    self.symbols[symbol]["closes"].append(float(line[row.index("Close")]))
                    self.symbols[symbol]["highs"].append(float(line[row.index("High")]))
                    self.symbols[symbol]["lows"].append(float(line[row.index("Low")]))
                    self.symbols[symbol]["opens"].append(float(line[row.index("Open")]))
                    self.symbols[symbol]["volumes"].append(float(line[row.index("Volume")]))
                x += 1

    def sma(self,symbol,statistic="closes"):
        if statistic in list(self.symbols[symbol]) and not statistic == "datetimes":
            return sum(self.symbols[symbol][statistic])/len(self.symbols[symbol][statistic])
        else:
            return "error:symbol or statistic not found"
        
    def max_volume(self,symbol):
        h = finance_data.fast_tabel(symbol)
        print(h["Volume"])
    
    def get_data(self,symbol,statistic):
        if statistic in list(self.symbols[symbol]):
            return self.symbols[symbol][statistic]
        else:
            return "error:symbol or statistic not found"
    
    def get_all_data(self,symbol):
        return self.symbols[symbol]
    
    def up_to_date_price(self,symbol):
        return finance_data.search_comp(symbol)
    
    def excpected_dividends(self,symbol):
        return finance_data.get_dividends(symbol)
