N, K = map(int, input().split())
S = list()
for i in range(K):
    S.append(input())

S.sort()

for i in range(K):
    print(S[i])


