#!/usr/bin/env python
from yahoo_finance import Share
import operator

def getStockPrices(stocks):
  #stocks must be an array of stock symbol strings
  
  # Refresh stock prices
  [Share(symbol).refresh() for symbol in stocks]
  
  # Return list of new prices
  return dict(zip(stocks,[Share(symbol).get_price() for symbol in stocks]))

def getFastestChangingPrices(oldstockprices,newstockprices):
  #stock prices must be dicts in the form (symbol,price)
  
  pdiff = dict()
  ptop = dict()
  for sym in newstockprices:
    pdiff[sym] = str((float(newstockprices[sym])-float(oldstockprices[sym]))/float(oldstockprices[sym])*100)
  
  pdiff = sorted(pdiff.items(), key=operator.itemgetter(1), reverse=True)
  return pdiff[:4]