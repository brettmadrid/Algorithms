#!/usr/bin/python

import sys


def making_change(amount, denominations):
    # create a zero padded list size of incoming amount + 1
    count = [0 for x in range(amount+1)]

    # set first array position value to equal 1
    count[0] = 1

    # loop through all possible coin values in denominations array
    for i in range(0, len(denominations)):  # for 0 to 4

        for j in range(denominations[i], amount+1):

            count[j] += count[j-denominations[i]]

    return count[amount]

# i = 2       to 4
# j = 10       to 5
# count = [1,1,1,1,1,2]
# count[5] += count[0] = 1


denominations = [1, 5, 10, 25, 50]
amount = 300
print(making_change(amount, denominations))

# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")
