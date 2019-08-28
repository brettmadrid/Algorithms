#!/usr/bin/python

import argparse
import math 

def find_max_profit(prices):
  # start with base value of neg infinity to account for any other neg values being more positive 
  max_prof = -math.inf

  for i, price in enumerate(prices):
    future_val = prices[i+1:]
    if future_val:
      max_price = max(future_val)
      current = max_price - price
      if current > max_prof:
        max_prof = current

  return max_prof
    
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))