S = input()
T = input()
s_cnt = [0 for _ in range(26)]
s_at = 0
t_cnt = [0 for _ in range(26)]
t_at = 0
for x in S:
    if x != "@":
        s_cnt[ord(x) - ord("a")] += 1
    else:
        s_at += 1

for x in T:
    if x != "@":
        t_cnt[ord(x) - ord("a")] += 1
    else:
        t_at += 1

cheat = ["a", "t", "c", "o", "d", "e", "r"]

for c in cheat:
    idx = ord(c) - ord("a")
    m = max(s_cnt[idx], t_cnt[idx])
    if s_at < m - s_cnt[idx] or t_at < m - t_cnt[idx]:
        print("No")
        exit()
    s_at -= m - s_cnt[idx]
    s_cnt[idx] = m
    t_at -= m - t_cnt[idx]
    t_cnt[idx] = m

print("Yes" if s_cnt == t_cnt else "No")
