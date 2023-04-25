import sys
import heapq as hq
input = sys.stdin.readline

def solution(n: int, m: int, board: list) -> int:
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    que = []
    hq.heappush(que, (-board[0][0], 0, 0))

    while que:
        _, cx, cy = hq.heappop(que)

        for i in range(4):
            nx = cx + dxy[i][0]
            ny = cy + dxy[i][1]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] < board[cx][cy]:
                if visited[nx][ny] == 0:
                    hq.heappush(que, (-board[nx][ny], nx, ny))
                visited[nx][ny] += visited[cx][cy]
    
    return visited[-1][-1] 

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))