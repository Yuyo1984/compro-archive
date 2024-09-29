#!/usr/bin/env python3

"""
File: main.py
Description:
Author:Yuyo1984
Date: 2024-07-
"""

# func


def main():
    # input
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a
    # solve
    ans = 3
    x = a - b
    y = (a + b) / 2
    z = b - a

    if x == 0:
        ans -= 1

    if z == 0:
        ans -= 1
    if not (y.is_integer()):
        ans -= 1
    # output
    print(ans)


if __name__ == "__main__":
    main()
