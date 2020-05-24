#!/bin/python3
""" Calculating the amount of valleys in a hiker path
"""

import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    """
    :param n: amount of steps
    :param ar: array with steps
    :return: count of valleys
    """
    h = 0
    scale = []
    valley = 0

    for step in s:
        if step == 'D':
            h -= 1
        if step == 'U':
            h += 1

        scale.append(h)

    for i in range(0, len(scale)):
        if scale[i] == 0:
            if scale[i - 1] < 0:
                valley += 1


    return valley


if __name__ == '__main__':
    n = int(sys.argv[1])
    s = sys.argv[2]
    result = countingValleys(n, s)
    print(result)