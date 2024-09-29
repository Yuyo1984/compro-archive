from bisect import bisect_right as br
from itertools import accumulate

N, X, Y = map(int, input().split())
A = [*map(int, input().split())]
A.sort(reverse=True)
B = [*map(int, input().split())]
B.sort(reverse=True)
acc_a = list(accumulate(A))
acc_b = list(accumulate(B))

idx_a = br(acc_a, X)
idx_b = br(acc_b, Y)

ans = min(idx_a, idx_b)
if ans < N:
    ans += 1
print(ans)
