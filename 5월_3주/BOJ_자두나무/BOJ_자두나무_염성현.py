import sys
input = lambda : sys.stdin.readline().strip()

T, W = map(int,input().split())
graph = []

for _ in range(T):
    graph.append(int(input()))

dp = [[[0]*3 for _ in range(W+2)] for _ in range(T+1)]

for i, g in enumerate(graph):
    for w in range(W+1):
        if w > i:
            continue
        if i == 0:
            if g == 1:
                dp[i+1][w][g] = 1
            else:
                dp[i+1][w+1][g] = 1
        else:
            # stay +1
            dp[i+1][w][g] = max(dp[i+1][w][g], dp[i][w][g] + 1)
            # stay +0
            dp[i+1][w][g%2+1] = max(dp[i+1][w][g%2+1], dp[i][w][g%2+1])
            # move +1
            dp[i+1][w+1][g] = max(dp[i+1][w+1][g], dp[i][w][g%2+1] + 1)
            # move +0
            dp[i+1][w+1][g%2+1] = max(dp[i+1][w+1][g%2+1], dp[i][w][g])
answer = 0
for d in dp[-1][:W+1]:
    answer = max(answer,max(d))
print(answer)