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
    n, t, a = map(int, input().split())
    # solve
    flag = True
    x = n - t - a
    if t < a:
        if t + x > a:
            flag = False
    else:
        if a + x > t:
            flag = False

    # output
    print("Yes" if flag else "No")


if __name__ == "__main__":
    main()
