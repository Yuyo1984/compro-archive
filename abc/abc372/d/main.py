# 解説AC

# func


def main():
    # input
    N = int(input())
    H = [*map(int, input().split())]
    # solve
    ans = []
    st = []
    for h in H[::-1]:
        ans.append(len(st))
        while st and st[-1] < h:
            st.pop()
        st.append(h)
    # output
    print(*ans[::-1])


if __name__ == "__main__":
    main()
