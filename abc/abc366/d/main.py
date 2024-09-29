#!/usr/bin/env python3

"""
File: main.py
Description:
Author:Yuyo1984
Date: 2024-07-
"""


# func
def threeD_accumulate(arr):
    x, y, z = len(arr), len(arr[0]), len(arr[0][0])
    csum = [[[0 for i in range(z + 1)] for j in range(y + 1)] for k in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            for k in range(1, z + 1):
                csum[i][j][k] = (
                    arr[i - 1][j - 1][k - 1]
                    + csum[i - 1][j][k]
                    + csum[i][j - 1][k]
                    + csum[i][j][k - 1]
                    - csum[i - 1][j - 1][k]
                    - csum[i - 1][j][k - 1]
                    - csum[i][j - 1][k - 1]
                    + csum[i - 1][j - 1][k - 1]
                )

    return csum


def range_sum(csum, x1, x2, y1, y2, z1, z2):
    return (
        csum[x2][y2][z2]
        - csum[x1 - 1][y2][z2]
        - csum[x2][y1 - 1][z2]
        - csum[x2][y2][z1 - 1]
        + csum[x1 - 1][y1 - 1][z2]
        + csum[x1 - 1][y2][z1 - 1]
        + csum[x2][y1 - 1][z1 - 1]
        - csum[x1 - 1][y1 - 1][z1 - 1]
    )


def main():
    # input
    n = int(input())
    arr = list()
    for i in range(n):
        L1 = list()
        for j in range(n):
            L2 = [*map(int, input().split())]
            L1.append(L2)
        arr.append(L1)

    # print(arr)
    # solve
    csum = threeD_accumulate(arr)
    # print(csum)
    Q = int(input())
    for i in range(Q):
        x1, x2, y1, y2, z1, z2 = map(int, input().split())
        res = range_sum(csum, x1, x2, y1, y2, z1, z2)
        print(res)
    # output


if __name__ == "__main__":
    main()
