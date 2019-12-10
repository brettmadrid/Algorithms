#!/usr/bin/python

import argparse
import math


def find_max_profit(prices):
    # stores the highest profit, start with neg infinity to account for neg calculated profit
    max_prof = -math.inf

    for i, sell_price in enumerate(prices):

        # create list comprehension of all remaining values to the right of i
        # these values represent subsequent prices in time
        future_val = prices[i+1:]

        if future_val:  # if there exist any remaining sell values to the right

            max_price = max(future_val)  # find max value in future_val list

            calc_profit = max_price - sell_price

            if calc_profit > max_prof:  # if calc_profit is more than currently stored max_prof
                max_prof = calc_profit  # set new max_prof to calculated profit

    return max_prof


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
