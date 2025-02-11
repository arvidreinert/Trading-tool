import read_data as rd
from datetime import datetime
import finance_data as fd
from time import sleep
from random import uniform

class sim():
    def __init__(self,cash):
        self.stocks = {}
        self.cash = cash

    def portfolio(self):
        print(f"Portfolio   {datetime.now().strftime("%Y_%m_%d %H:%M:%S")}")
        print("cash:"+str(round(self.cash,3)))
        for stock in self.stocks:
            base = f"\n{stock}:"
            c = 1
            for order in self.stocks[stock]["orders"]:
                base+=f"\n  order ({c})\n\t"
                gain = (order["pwb"]-fd.search_comp(stock))*order["amount"]*order["kind"]
                base+=f"amount:{order["amount"]}, kind:{"long" if order["kind"]== 1 else "short"}, {"gain" if gain >= 0 else "loss"}:{gain}"
                c += 1
            print(base)
            
    def buy_order(self,symbol,amount,kind="long"):
        if kind == "long":
            kind = 1
        else:
            kind = -1
        if not symbol in self.stocks:
            self.stocks[symbol] = {"amount":0,"orders":[]}

        dlay = round(uniform(0,2), 2)
        sleep(dlay)
        self.stocks[symbol]["orders"].append({"amount":amount,"kind":kind,"pwb":fd.search_comp(symbol)})
        self.stocks[symbol]["amount"] += amount
        if kind == 1:
            self.cash -= amount * fd.search_comp(symbol)
        return "order completed with "+str(dlay)+" seconds of delay; price: "+str(fd.search_comp(symbol))
    
    def sell_order(self,symbol,amount,kind="long"):
        pass

"""symbol = "VSE"
chunk = rd.data_chunk()
fd.create_data(symbol, interval="1h",duration={ "days": 3,"hours": 0,"minutes": 0,"seconds": 0 })
chunk.add_symbol(symbol)
chunk.save_data(symbol)"""

simulator = sim(100)
simulator.buy_order("AAPL",1)
simulator.buy_order("GOOG",7)
simulator.buy_order("AAPL",5,kind="short")
simulator.portfolio()