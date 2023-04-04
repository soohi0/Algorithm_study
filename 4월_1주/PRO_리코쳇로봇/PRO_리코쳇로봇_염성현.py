from collections import deque

def move(x, y, b, d):
    nx, ny = x, y
    while 0<=nx<len(b) and 0<=ny<len(b[0]) and b[nx][ny] != 'D':
        nx = nx + d[0]
        ny = ny + d[1]
    nx = nx - d[0]
    ny = ny - d[1]
    return nx, ny

def bfs(sx, sy, b, v, d):
    queue = deque()
    queue.append((sx,sy,0))
    v[sx][sy] = True
    while queue:
        cx, cy, cnt = queue.popleft()
        if b[cx][cy] == 'G':
            return cnt
        if not v[cx][cy]:
            v[cx][cy] = True
        for e in d:
            nx, ny = move(cx,cy,b,e)
            if not v[nx][ny]:
                queue.append((nx,ny,cnt+1))
    return -1
                
def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                rx, ry = i, j
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    visited = [[False]*len(board[0]) for _ in range(len(board))]
    answer = bfs(rx,ry,board,visited,direction)
    return answer