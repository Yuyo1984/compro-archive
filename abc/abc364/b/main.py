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
    h, w = map(int, input().split())
    Si, Sj = map(lambda x: int(x) - 1, input().split())
    grid = list(list(input()) for _ in range(h))
    query = input()
    # solve
    now = [Si, Sj]
    for c in query:
        if c == "U":
            x = now[0] - 1
            y = now[1]
        elif c == "L":
            x = now[0]
            y = now[1] - 1
        elif c == "R":
            x = now[0]
            y = now[1] + 1
        else:
            x = now[0] + 1
            y = now[1]
        if 0 <= x < h and 0 <= y < w and grid[x][y] == ".":
            now = [x, y]

    # output
    print(now[0] + 1, now[1] + 1)


if __name__ == "__main__":
    main()
