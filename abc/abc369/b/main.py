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
    A_l = list()
    A_r = list()
    for i in range(N):
        a, s = input().split()
        if s == "L":
            A_l.append(int(a))
        else:
            A_r.append(int(a))

    # solve
    ans = 0
    for i in range(len(A_l) - 1):
        ans += abs(A_l[i + 1] - A_l[i])
    for i in range(len(A_r) - 1):
        ans += abs(A_r[i + 1] - A_r[i])

    # output
    print(ans)


if __name__ == "__main__":
    main()
