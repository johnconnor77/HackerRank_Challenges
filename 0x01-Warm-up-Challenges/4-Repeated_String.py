#!/bin/python3
""" lilah infinite repeated string
"""
import math
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    """
    Calculating occurences at infinite string of len eq n
    :param s: substring
    :param n: len of lilah string
    :return: occurences at lilah string of 'a' char
    """

    times_a = s.count('a')
    res = n % len(s)

    repeated = int(n / len(s)) * times_a

    if res == 0:
        return repeated
    else:
        subs = s[0:res]
        return repeated + subs.count('a')


if __name__ == '__main__':
    n = int(sys.argv[2])
    s = sys.argv[1]

    result = repeatedString(s, n)
    print(result)
