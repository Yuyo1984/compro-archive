# 解説AC
# disjoint set union
class DSU:
    # 初期化
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.member = [[i] for i in range(n)]

    # 親が何なのか調べる
    def find(self, u):
        if self.parents[u] < 0:
            return u
        else:
            self.parents[u] = self.find(self.parents[u])
            return self.parents[u]

    # 同じグループに統合
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return

        if self.parents[u] > self.parents[v]:
            u, v = v, u

        self.parents[u] += self.parents[v]
        self.parents[v] = u

        self.member[u] += self.member[v]
        self.member[u] = sorted(self.member[u], reverse=True)[:10]


# 具体例
def main():
    N, Q = map(int, input().split())
    dsu = DSU(N + 1)

    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            u, v = q[1:]
            dsu.union(u, v)

        else:
            v, k = q[1:]
            v = dsu.find(v)

            if len(dsu.member[v]) < k:
                print(-1)
            else:
                print(dsu.member[v][k - 1])


if __name__ == "__main__":
    main()
