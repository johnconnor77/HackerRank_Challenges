#!/bin/python3
""" Jumping on the clouds
    Emma has to void clouds with thunders
"""

import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    """
    :param c: array with clouds sequece
    :return: jumps that emma has to make
    """
    i = 0
    jumps = 0

    while i < len(c) - 1:
        try:
            if c[i + 2] == 0:
                    jumps += 1
                    i += 2
                    continue
        except IndexError:
            pass
        if c[i + 1] == 0:
            jumps += 1
            i += 1
            continue

    return jumps


if __name__ == '__main__':
    n = int(sys.argv[1])
    c = [int(i) for i in sys.argv[2:]]

    result = jumpingOnClouds(c)
    print(result)
