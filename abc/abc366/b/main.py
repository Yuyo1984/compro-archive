#!/usr/bin/env python3

"""
File: main.py
Description:
Author:Yuyo1984
Date: 2024-07-
"""

# func


def rotate(grid):
    grid = grid[::-1]
    grid = list(map(list, zip(*grid)))
    return grid


def main():
    # input
    n = int(input())
    S = [list(input()) for i in range(n)]
    # solve
    x = 0
    for i in range(n):
        x = max(x, len(S[i]))

    T = [list() for i in range(x)]

    for i in range(n - 1, -1, -1):
        for j in range(x):
            if j < len(S[i]):
                T[j].append(S[i][j])
            else:
                T[j].append("*")

    for i in range(x):
        while T[i][-1] == "*":
            T[i].pop()

    # output
    for i in range(x):
        print("".join(T[i]))


if __name__ == "__main__":
    main()
