#!/usr/bin/env python3

"""
File: main.py
Description:
Author:Yuyo1984
Date: 2024-07-
"""

# func
from collections import defaultdict


def main():
    # input
    q = int(input())
    d = defaultdict(int)
    num = 0
    for i in range(q):
        query = list(input().split())
        type = query[0]
        if type == "1":
            x = int(query[1])
            d[x] += 1
            if d[x] == 1:
                num += 1
        elif type == "2":
            x = int(query[1])
            d[x] -= 1
            if d[x] == 0:
                num -= 1
        else:
            print(num)
    # solve

    # output


if __name__ == "__main__":
    main()
