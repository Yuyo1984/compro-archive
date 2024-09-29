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
    S = input()
    # solve
    ansl = []
    for x in S:
        if x != ".":
            ansl.append(x)
    # output
    print("".join(ansl))


if __name__ == "__main__":
    main()
