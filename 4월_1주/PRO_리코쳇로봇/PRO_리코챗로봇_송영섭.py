from collections import deque
# bfs 로 구현

def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    que = deque([(i, j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j] == "R"])
    pos_d = set([(i, j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j] == "D"])
    loc_g = [(i, j) for j in range(len(board[0])) for i in range(len(board)) if board[i][j] == "G"][0]

    visited = [[-1] * len(board[0]) for _ in range(len(board))]
    visited[que[0][0]][que[0][1]] = 0
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            tmp_x, tmp_y = x, y
            while ((tmp_x, tmp_y) not in pos_d) and (0 <= tmp_x < len(board) and 0 <= tmp_y < len(board[0])):
                tmp_x += dx[i]
                tmp_y += dy[i]
            tmp_x -= dx[i]
            tmp_y -= dy[i]
            if 0 <= tmp_x < len(board) and 0 <= tmp_y < len(board[0]):
                if visited[tmp_x][tmp_y] == -1:
                    que.append((tmp_x, tmp_y))
                    visited[tmp_x][tmp_y] = visited[x][y] + 1
            
    return visited[loc_g[0]][loc_g[1]]