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
    N = int(input())
    A = [*map(int, input().split())]
    # solve
    # dp1が偶数、dp2が奇数
    dp1 = 0
    dp2 = -float("inf")

    for i in range(N):
        x = A[i]
        tmp = dp1
        dp1 = max(dp2 + 2 * x, dp1)
        dp2 = max(tmp + x, dp2)

    # output
    print(max(dp1, dp2))


if __name__ == "__main__":
    main()
