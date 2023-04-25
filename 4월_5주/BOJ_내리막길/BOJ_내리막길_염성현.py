import sys 
sys.setrecursionlimit(10000)
input = lambda : sys.stdin.readline().strip()
M, N = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
d = [(0,1),(0,-1),(1,0),(-1,0)]
answer = 0 

def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0

        for dx, dy in d:
            nx = x + dx
            ny = y + dy 
            if 0<=nx<M and 0<=ny<N:
                if graph[x][y] > graph[nx][ny]:
                    dp[x][y] += dfs(nx,ny)
    return dp[x][y] 

print(dfs(0,0))
print(dp)

# def dfs(x,y)
#     queue = []
#     queue.append((x,y))
#     answer = 0
#     visited[x][y] = True 
#     while queue:
#         qx, qy = queue.pop()
#         if (qx,qy) == (M-1,N-1):
#             answer +=1
#         for dx, dy in d:
#             nx = dx+qx
#             ny = dy+qy
#             if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
#                 if graph[nx][ny]<graph[x][y]:
#                     visited[nx][ny] = True
#                     queue.append((nx,ny))
#     if answer > 0:
#         return answer 
#     else:
#         return -1

# print(dfs(0,0))