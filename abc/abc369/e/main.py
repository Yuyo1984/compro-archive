#!/usr/bin/env python3

"""
File: main.py
Description:
Author:Yuyo1984
Date: 2024-07-
"""

# func
import itertools

INF = float("inf")


def floyd_warshall(graph):
    V = len(graph)

    dist = [[INF] * V for i in range(V)]

    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def solve(k, b, dist, edges):
    ans = INF
    n = len(dist)
    for P in itertools.permutations(range(k)):
        l = 0
        lp = 0
        r = 0
        rp = 0

        for p in P:
            u, v, t = edges[b[p] - 1]
            nr = min(l + dist[lp][u], r + dist[rp][u]) + t
            nl = min(l + dist[lp][v], r + dist[rp][v]) + t
            l, lp = nl, u
            r, rp = nr, v
        ans = min(l + dist[lp][n - 1], r + dist[rp][n - 1], ans)

    return ans


def main():
    # input
    n, m = map(int, input().split())
    graph = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    edges = list()
    for i in range(m):
        u, v, t = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = min(graph[u][v], t)
        graph[v][u] = min(graph[v][u], t)
        edges.append((u, v, t))

    dist = floyd_warshall(graph)

    # solve
    ans = INF
    q = int(input())
    for i in range(q):
        k = int(input())
        b = [*map(int, input().split())]
        ans = solve(k, b, dist, edges)
        print(ans)
    # output


if __name__ == "__main__":
    main()
