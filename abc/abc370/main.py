from bisect import bisect_left as bl
from bisect import bisect_right as br
from collections import defaultdict

H, W, Q = map(int, input().split())
queries = list()
for _ in range(Q):
    r, c = map(int, input().split())
    queries.append((r, c))

grid = defaultdict(list)
for i in range(1, H + 1):
    grid[i].append([i for i in range(1, W + 1)])

for q in queries:
    x = q[0]
    y = q[1]
    if y in grid[x]:
        grid[x].remove(y)
    else:
        idx1 = br(grid[y], x) - 1
        if idx1 >= 0:
            grid[y].remove(grid[y][idx1])


ans = len(grid)
print(ans)
