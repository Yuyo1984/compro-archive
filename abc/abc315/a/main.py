from sys import stdin
input = stdin.readline

S = input().rstrip()
ansl = []
for i in range(len(S)):
    if S[i] != 'a' and S[i] != 'i' and S[i] != 'u' and S[i] != 'e' and S[i] != 'o':
        ansl.append(S[i])

print("".join(ansl))
