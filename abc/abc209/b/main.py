from sys import stdin
input = stdin.readline

N, X = map(int, input().split())
A = [*map(int, input().split())]

if X >= sum(A) - N //2:
    print("Yes")
else:
    print("No")
