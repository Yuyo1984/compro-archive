# 解説AC

# func


def main():
    # input
    N = int(input())
    A = [*map(int, input().split())]
    W = [*map(int, input().split())]
    max_w = [0 for i in range(N)]
    for i in range(N):
        x = A[i] - 1
        max_w[x] = max(max_w[x], W[i])
    # solve
    # 答えは重さの総和から各箱の荷物の重さの最大値の和を引いたもの
    # なぜなら、それ以外の荷物は全てどこかの箱に移動されることになるから、
    # その分コストを支払うことになる。
    # 荷物と箱の数が等しくなってるから１対１対応できることに着目する。
    # ざっくりいうと、総コストから支払う必要のないコストを引いてるだけ。

    sum_w = sum(W)
    sum_max = sum(max_w)

    ans = sum_w - sum_max

    # output
    print(ans)


if __name__ == "__main__":
    main()
