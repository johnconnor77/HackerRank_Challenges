#!/bin/python3
""" SockMerchant function that found the socks that could
    be paired of the same color
"""

import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    """
    :param n: amount of elements in ar
    :param ar: array with colors of sock as numbers
    :return: paired socks
    """
    ar.sort()
    aux = []
    aux = ar.copy()
    i = 0

    while i <= n - 2:
        aux1 = ar[i]
        aux2 = ar[i + 1]
        if ar[i] == ar[i + 1]:
            del ar[i:i + 2]
            n = len(ar)
            i = 0
        else:
            i += 1

    print(ar)
    print(aux)
    return int((len(aux) - len(ar)) / 2)


if __name__ == '__main__':
    n = int(sys.argv[1])
    ar = [int(i) for i in sys.argv[2:]]
    result = sockMerchant(n, ar)
    print(result)
