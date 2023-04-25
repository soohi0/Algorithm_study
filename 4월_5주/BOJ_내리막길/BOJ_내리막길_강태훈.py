import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = (1,-1,0,0)
dy = (0,0,1,-1)

def get_near(x, y, n, m):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            yield nx, ny

def main():
    m, n = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(m)]
    dp = [[-1]*n for _ in range(m)]

    def dfs(x, y):
        if (x,y) == (n-1,m-1):
            return 1
        if dp[y][x] != -1:
            return dp[y][x]
        dp[y][x] = 0
        for nx, ny in get_near(x, y, n, m):
            if heights[ny][nx] < heights[y][x]:
                dp[y][x] += dfs(nx, ny)
        return dp[y][x]
    print(dfs(0,0))

main()