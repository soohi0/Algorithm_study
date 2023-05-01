from collections import deque

while True:
    L, R, C = map(int,input().split())
    if (L,R,C) == (0,0,0):
        break
    graph = [[[]*C for _ in range(R+1)] for _ in range(L)]
    visited = [[[False]*C for _ in range(R+1)] for _ in range(L)]
    for k in range(L):
        for i in range(R+1):
            temp = list(input())
            graph[k][i] = temp
            if len(temp) > 0:
                for j, t in enumerate(temp):
                    if t == 'S':
                        starting = (k,i,j)

    d = [(-1,0,0),(1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

    queue = deque([])
    queue.append((*starting,0))
    visited[starting[0]][starting[1]][starting[2]] = True 
    flag = 0
    while queue:
        qx, qy, qz, cnt = queue.popleft()
        if graph[qx][qy][qz] == 'E':
            print('Escaped in {} minute(s).'.format(cnt))
            flag = 1
            break 
        for dx, dy, dz in d:
            nx = qx + dx 
            ny = qy + dy 
            nz = qz + dz 
            if 0<=nx<L and 0<=ny<R and 0<=nz<C and not visited[nx][ny][nz]:
                if graph[nx][ny][nz] == '.' or graph[nx][ny][nz] == 'E':
                    visited[nx][ny][nz] = True 
                    queue.append((nx,ny,nz,cnt+1))
    if flag == 0:
        print('Trapped!')