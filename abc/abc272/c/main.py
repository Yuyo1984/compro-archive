from typing import List

N = int(input())
A = [*map(int, input().split())]
odd_L = list()
even_L = list()
for x in A:
    if x % 2 == 0:
        even_L.append(x)
    else:
        odd_L.append(x)
even_L.sort(reverse=True)
odd_L.sort(reverse=True)

x = -1
y = -1
if len(even_L) >= 2:
    x = even_L[0] + even_L[1]
if len(odd_L) >= 2:
    y = odd_L[0] + odd_L[1]
print(max(x, y))
