import sys
sys.setrecursionlimit(100000)
N = int(input())
A = list(map(int, input().split(" ")))

dp = [-1 for _ in range(N)]


def jump(x: int):
    if x == N - 1:
        return 0

    if dp[x] != -1:
        return dp[x]

    dp[x] = sys.maxsize

    for i in range(x + 1, N):
        dp[x] = min(dp[x], max(jump(i), (i - x) * (1 + abs(A[x] - A[i]))))

    return dp[x]


if __name__ == "__main__":
    print(jump(0))
