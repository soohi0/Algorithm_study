from collections import defaultdict
n = int(input())
graph = [[-1]*n for _ in range(n)]
favorites = defaultdict(list)
orders = []
for i in range(1,n*n+1):
    n0,n1,n2,n3,n4 = map(int, input().split())
    favorites[n0] = [n1,n2,n3,n4]
    orders.append(n0)
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for c in orders:
    pspace = []
    for x in range(n-1,-1,-1):
        for y in range(n-1,-1,-1):
            empty = 0
            friends = 0
            if graph[x][y] == -1:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<n and 0<=ny<n:
                        if graph[nx][ny] == -1:
                            empty += 1
                        elif graph[nx][ny] in favorites[c]:
                            friends += 1
                pspace.append([x,y,friends,empty])
    pspace.sort(lambda x: (-x[2],-x[3],x[0],x[1]))
    px,py,pf,pe = pspace[0]
    graph[px][py]=c
answer = 0
for gx in range(n):
    for gy in range(n):
        gnow = graph[gx][gy]
        gfriends = 0
        for i in range(4):
            ngx = gx + dx[i]
            ngy = gy + dy[i]
            if 0<=ngx<n and 0<=ngy<n:
                if graph[ngx][ngy] in favorites[gnow]:
                    gfriends += 1
        if gfriends >= 1:
            answer += 10 ** (gfriends -1)
print(answer)