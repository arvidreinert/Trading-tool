import read_data as rd
from datetime import datetime
import finance_data as fd
from time import sleep
from random import uniform
import ast

class sim():
    def __init__(self,cash):
        self.stocks = {}
        self.cash = cash

    def portfolio(self):
        print(f"Portfolio   {datetime.now().strftime("%Y_%m_%d %H:%M:%S")}")
        print("cash:"+str(round(self.cash,3)))
        for stock in self.stocks:
            base = f"\n{stock}  {self.stocks[stock]["amount"]}:"
            c = 1
            for order in self.stocks[stock]["orders"]:
                base+=f"\n  order ({c})\n\t"
                gain = (order["pwb"]-fd.search_comp(stock))*order["amount"]*order["kind"]
                base+=f"amount:{order["amount"]}, kind:{"long" if order["kind"] == 1 else "short" if order["kind"] == -1 else "sell"}, {"gain" if gain >= 0 else "loss"}:{gain}"
                c += 1
            print(base)
            
    def buy_order(self,symbol,amount,kind="long"):
        if not symbol in self.stocks:
            self.stocks[symbol] = {"amount":0,"longs":0,"shorts":0,"orders":[]}
        if kind == "long":
            self.stocks[symbol]["longs"] += amount
            kind = 1
        else:
            self.stocks[symbol]["shorts"] += amount
            kind = -1

        dlay = round(uniform(0,2), 2)
        sleep(dlay)
        self.stocks[symbol]["orders"].append({"amount":amount,"kind":kind,"pwb":fd.search_comp(symbol)})
        self.stocks[symbol]["amount"] += amount
        self.cash -= amount * fd.search_comp(symbol)

        return "order completed with "+str(dlay)+" seconds of delay; price: "+str(fd.search_comp(symbol))
    
    def sell_order(self,symbol,amount,kind="long"):
        cond = False
        if kind == "long" and self.stocks[symbol]["longs"] >= amount:
            cond = True
        if kind == "short" and self.stocks[symbol]["shorts"] >= amount:
            cond = True
        if cond:
            if kind == "long":
                self.stocks[symbol]["longs"] -= amount
                kind = 1
            else:
                self.stocks[symbol]["shorts"] -= amount
                kind = -1
            dlay = round(uniform(0,2), 2)
            sleep(dlay)
            self.stocks[symbol]["amount"] -= amount
            self.stocks[symbol]["orders"].append({"amount":amount,"kind":0,"pwb":fd.search_comp(symbol)})
            if kind == 1:
                self.cash += amount * fd.search_comp(symbol)
            else:
                self.cash += amount * fd.search_comp(symbol)
                self.cash -= amount*0.05
        if self.stocks[symbol]["amount"] == 0:
            del self.stocks[symbol]

    def save_sim(self,filename):
        with open(f"{filename}.txt", mode ='w')as file:
            file.write(f"stocks={self.stocks}\ncash={self.cash}")

    def load_sim(self,filename):
        with open(f"{filename}.txt", mode ='r')as file:
            t = file.read().split("\n")
            self.stocks = ast.literal_eval(t[0].split("=")[1])
            self.cash = float(t[1].split("=")[1])


"""symbol = "VSE"
chunk = rd.data_chunk()
fd.create_data(symbol, interval="1h",duration={ "days": 3,"hours": 0,"minutes": 0,"seconds": 0 })
chunk.add_symbol(symbol)
chunk.save_data(symbol)"""

simulator = sim(100)
simulator.buy_order("AAPL",1)
simulator.buy_order("AAPL",5,"short")
simulator.sell_order("AAPL",1)
simulator.sell_order("AAPL",5,"short")
simulator.buy_order("GOOG",7)
simulator.sell_order("GOOG",7)
simulator.portfolio()
simulator.save_sim("test")
simulator.load_sim("test")