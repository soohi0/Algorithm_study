from collections import deque

def solution(maps):
    # bfs
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = []
    
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            cnt = 0
            if maps[i][j] != 'X' and visited[i][j] == 0:
                que = deque()
                que.append((i, j))
                visited[i][j] = 1
                
                while que:
                    cx, cy = que.popleft()
                    cnt += int(maps[cx][cy])
                    for k in range(4):
                        nx = cx + dxy[k][0]
                        ny = cy + dxy[k][1]
                        if 0 <= nx < n and 0 <= ny < m:
                            if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                                que.append((nx, ny))
                                visited[nx][ny] = 1
                
                result.append(cnt)
                
    result.sort()
    
    return result if result else [-1]