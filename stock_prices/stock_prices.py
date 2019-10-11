#!/usr/bin/python

import argparse

#defining a function called find max profit that accept parameter of prices if the length of 
# proc less than of equal to return none
def find_max_profit(prices):
    if len(prices) <= 1:
        return None
    prior_smallest = prices[0]   #declaring array
    max_profit_so_far = prices[1] - prior_smallest #declaring max profit, first index s
    for i in range(1, len(prices) - 1):
        new_profit = prices[i] - prior_smallest #
        if new_profit > max_profit_so_far:
            max_profit_so_far = new_profit
        if prices[i] < prior_smallest:
            prior_smallest = prices[i]
    return max_profit_so_far


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))