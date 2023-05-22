from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def bfs(maps, x, y, visited):
    r, c = len(maps), len(maps[0])
    q = deque([])
    # list에 append
    q.append((x, y))
    visited[x][y] = True
    total = 0
    while q:
        qx, qy = q.popleft()
        total += int(maps[qx][qy])
        for i in range(4):
            nx, ny = qx + dx[i], qy + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 'X':
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    
    return total, visited

def solution(maps):
    r, c = len(maps), len(maps[0])
    maps = [list(m) for m in maps]
    visited = [[False]*c for _ in range(r)]
    
    answer = []
    for x in range(r):
        for y in range(c):
            if maps[x][y] != 'X' and not visited[x][y]:
                days, visited = bfs(maps, x, y, visited)
                answer.append(days)

    
    return sorted(answer) if answer else [-1]