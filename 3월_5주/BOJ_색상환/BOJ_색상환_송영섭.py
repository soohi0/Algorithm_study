import sys
sys.stdin = open("test.txt", "r")
input = sys.stdin.readline

N = int(input())
K = int(input())

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N+1):
    for j in range(K+1):
        if j == 0:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = i
        elif i / j >= 2:
            dp[i][j] = dp[i-1][j] + dp[i-2][j-1]
        dp[i][j] %= 1000000003

print(dp[N][K])