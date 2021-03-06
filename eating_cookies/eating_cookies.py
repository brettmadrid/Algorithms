#!/usr/bin/python

import sys
from functools import lru_cache
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

'''
0:1
1:1
2:2
3:4
4:7
5:13
6:24
7:44
8:81
9:149
10:274
'''


@lru_cache(maxsize=500)
def eating_cookies(n, cache=None):

    if n == 0:
        return 1
    if n <= 2:
        return n
    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
