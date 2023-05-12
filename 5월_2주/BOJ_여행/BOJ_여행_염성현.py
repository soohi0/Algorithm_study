import sys
input=sys.stdin.readline

N, M, K = map(int,input().split())
airline = [[0]*(N+1) for _ in range(N+1)]
dp = [[0]*(M+1) for _ in range(N+1)]
for _ in range(K):
    a, b, c = map(int, input().split())
    airline[a][b] = max(airline[a][b], c)
for i in range(2, N+1):
    dp[i][2] = airline[1][i]
for i in range(2, N+1):
    for j in range(3, M+1):
        for l in range(1, i):
            if airline[l][i] and dp[l][j-1]:
                dp[i][j] = max(dp[l][j-1]+airline[l][i], dp[i][j])
print(max(dp[N]))