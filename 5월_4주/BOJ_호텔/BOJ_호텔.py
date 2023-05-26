import sys 
input = lambda : sys.stdin.readline().strip()

C, N = map(int,input().split())
graph = list()
for _ in range(N):
    graph.append(list(map(int,input().split())))
    
dp = [1e9 for _ in range(C+100)]
dp[0] = 0
for i in range(C+100):
    for cost, g in graph:
        if i-g >= 0:
            dp[i] = min(dp[i], dp[i-g]+cost)
print(min(dp[C:]))