import ccxt
from decimal import *
import time
from win10toast import ToastNotifier

exchange = ccxt.whitebit()
pair = input("pair: ")
pair = pair.upper()
go = True


def setup():
    price = input("notify at what price: ")        
    price = Decimal(price)
    return price
    
def checkprice(symbol, api):
    ticker = api.fetch_ticker(symbol)
    smbl_ask = ticker['ask']
    smbl_bid = ticker['bid']
    
    return Decimal(smbl_ask), Decimal(smbl_bid)
    
    
def notifycheck(price, pair, api):
    stop = False
    while stop == False:
        current_price, current_ask = checkprice(pair, api)
        if Decimal(current_price) >= price:
            notify_str = pair + " price reached " + str(current_price) + "ask is " + str(current_ask)
            toaster = ToastNotifier()
            toaster.show_toast(title = 'Price target met', message = notify_str)
            stop = True
            
        else:
            time.sleep(2)
            pass
        
        
      

    
while go == True:
    target = setup()
    
    notifycheck(target, pair, exchange)
    cont = input("keep going y/n: ")
    if cont == 'y' or 'Y':
        pass
    if cont == 'n' or 'N':
        go = False
    else:
        go = True
    
    

    