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
    diff = list()
    for i in range(N - 1):
        x = A[i + 1] - A[i]
        diff.append(x)
    # solve
    ans = 2 * N - 1
    checker = 0
    if len(diff) > 0:
        checker = diff[0]
    count = 0
    for i in range(1, len(diff)):
        if checker == diff[i]:
            count += 1
        else:
            ans += count * (count + 1) // 2
            count = 0
            checker = diff[i]

    ans += count * (count + 1) // 2

    # output
    print(ans)


if __name__ == "__main__":
    main()
