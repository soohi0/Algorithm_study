import sys
from collections import deque
input = sys.stdin.readline

def solution(l: int, r: int, c: int, board: list) -> str:
    dxyz = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    start, end = None, None
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if board[i][j][k] == "S":
                    start = (i, j, k)
                if board[i][j][k] == "E":
                    end = (i, j, k)

    visited = [[[-1] * c for _ in range(r)] for _ in range(l)]
    visited[start[0]][start[1]][start[2]] = 0
    que = deque()
    que.append(start)

    while que:
        cur_z, cur_x, cur_y = que.popleft()
        for i in range(6):
            dx = cur_x + dxyz[i][1]
            dy = cur_y + dxyz[i][2]
            dz = cur_z + dxyz[i][0]
            if 0 <= dz < l and 0 <= dx < r and 0 <= dy < c:
                if board[dz][dx][dy] != '#' and visited[dz][dx][dy] == -1:
                    que.append((dz, dx, dy))
                    visited[dz][dx][dy] = visited[cur_z][cur_x][cur_y] + 1

    return f"Escaped in {visited[end[0]][end[1]][end[2]]} minute(s)." if visited[end[0]][end[1]][end[2]] != -1 else "Trapped!"


if __name__ == "__main__":
    while True:
        L, R, C = map(int, input().split())
        if L == 0 and R == 0 and C == 0:
            break

        board = []
        for i in range(L):
            tmp = [list(map(str, input())) for _ in range(R)]
            _ = input()
            board.append(tmp)

        print(solution(L, R, C, board))