# func


def main():
    # input
    N, Q = map(int, input().split())
    S = list(input())
    a_idx = set()
    b_idx = set()
    c_idx = set()
    for i in range(N):
        if S[i] == "A":
            a_idx.add(i)
        if S[i] == "B":
            b_idx.add(i)
        if S[i] == "C":
            c_idx.add(i)

    cnt = 0
    for x in a_idx:
        if x + 1 in b_idx and x + 2 in c_idx:
            cnt += 1

    # solve
    for i in range(Q):
        x, c = input().split()
        x = int(x) - 1
        if x in a_idx:
            a_idx.discard(x)
            if x + 1 in b_idx and x + 2 in c_idx:
                cnt -= 1
        if x in b_idx:
            b_idx.discard(x)
            if x - 1 in a_idx and x + 1 in c_idx:
                cnt -= 1
        if x in c_idx:
            c_idx.discard(x)
            if x - 2 in a_idx and x - 1 in b_idx:
                cnt -= 1

        if c == "A":
            a_idx.add(x)
            if x + 1 in b_idx and x + 2 in c_idx:
                cnt += 1
        elif c == "B":
            b_idx.add(x)
            if x - 1 in a_idx and x + 1 in c_idx:
                cnt += 1
        elif c == "C":
            c_idx.add(x)
            if x - 2 in a_idx and x - 1 in b_idx:
                cnt += 1

        print(cnt)

    # output


if __name__ == "__main__":
    main()
