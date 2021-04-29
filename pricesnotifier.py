import ccxt
import urllib
import json
import pickle
from decimal import *
import time
from win10toast import ToastNotifier

exchange = ccxt.whitebit()
pair = input("pair: ")
pair = pair.upper()
go = True

def update_bsc_tokens():
    bsc_list = pickle.load(open("tokens.p", "rb"))
    return bsc_list


def setup_exch_cmd():
    price = input("notify at what price: ")        
    price = Decimal(price)
    return price
    
def checkprice(symbol, api):
    ticker = api.fetch_ticker(symbol)
    smbl_ask = ticker['ask']
    smbl_bid = ticker['bid']
    
    return Decimal(smbl_ask), Decimal(smbl_bid)

#checks prices for tokens in bsc tokens list    
def checkprices_pancake(contracts):
    done = 0
    pricelist = {}
    url = 'https://api.pancakeswap.info/api/tokens'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    pnck = urllib.request.urlopen(req)
    pnck_raw = pnck.read()
    encoding = pnck.info().get_content_charset()
    pnck_list = json.loads(pnck_raw.decode(encoding))
     
    key_list = pnck_list['data']
      
    for addresses, coin_info in key_list.items():
             
        if coin_info['name'] in contracts:
                 
            pricelist[coin_info['name']] = Decimal(coin_info['price'])
                 
    return pricelist        
        
    
#used in exchange_pricenotifier to check the price    
def notify_check_cex(price, pair, api):
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
        
           
#this should be run in a separate thread
#used to notify of price target met on CEX
def exchange_pricenotifier(target, pair, exchange):    
    while go == True:
        target = setup_exch_cmd()
        
        notify_check_cex(target, pair, exchange)
        cont = input("keep going y/n: ")
        if cont == 'y' or 'Y':
            pass
        if cont == 'n' or 'N':
            go = False
        else:
            go = True
    
    


tokenlist = update_bsc_tokens()
pancakelist = checkprices_pancake(tokenlist)
print(pancakelist)