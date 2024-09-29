#!/usr/bin/env python3

"""
File: main.py
Description:
Author:Yuyo1984
Date: 2024-07-
"""

# func
import math


def main():
    # input
    M = int(input())
    # solve
    ansl = list()
    while M > 0:
        x = int(math.log(M, 3))
        ansl.append(x)
        M -= 3**x
    # output
    print(len(ansl))
    print(*ansl)


if __name__ == "__main__":
    main()
