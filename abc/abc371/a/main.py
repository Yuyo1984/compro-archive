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
    r = list()
    x = input().rsplit()
    for v in x:
        if v == "<":
            r.append("0")
        else:
            r.append("1")
    r = "".join(r)
    # solve
    ans = ""
    if r == "000" or r == "111":
        ans = "B"
    elif r == "011" or r == "100":
        ans = "A"
    else:
        ans = "C"

    # output
    print(ans)


if __name__ == "__main__":
    main()
