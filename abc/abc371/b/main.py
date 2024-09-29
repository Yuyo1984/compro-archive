def main():
    # input
    n, m = map(int, input().split())
    children = [[] for _ in range(n + 1)]
    flag = [True for _ in range(n + 1)]
    data = list()

    # solve
    for i in range(m):
        a, b = input().split()
        a = int(a)
        children[a].append(b)
        data.append((a, b))

    # output
    for v in data:
        if flag[v[0]] and v[1] == "M":
            print("Yes")
            flag[v[0]] = False
        else:
            print("No")


if __name__ == "__main__":
    main()
