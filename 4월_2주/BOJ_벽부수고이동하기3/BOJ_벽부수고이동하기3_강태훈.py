# import sys
# input = sys.stdin.readline

# from heapq import heappop, heappush

# dx = [-1,1,0,0]
# dy = [0,0,1,-1]
# def get_near(n,m,x,y):
#     for i in range(4):
#         nx, ny = x+dx[i], y+dy[i]
#         if 0<=nx<m and 0<=ny<n:
#             yield nx, ny

# def solve(n, m, k, board):
#     visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
#     hq = []
#     hq.append([1,0,(0,0,1)])
#     visited[0][0][0] = 1
#     while hq:
#         cnt, break_cnt, (x, y, is_moring) = heappop(hq)
#         if x==m-1 and y==n-1:
#             return cnt
#         for nx, ny in get_near(n,m,x,y):
#             n_is_morning = (is_moring+1)%2
#             if board[ny][nx]=="0":
#                 if visited[break_cnt][ny][nx]:
#                     continue
#                 heappush(hq, [cnt+1, break_cnt, (nx, ny, n_is_morning)])
#                 visited[break_cnt][ny][nx] = 1
#             else:
#                 if break_cnt < k and is_moring:
#                     if visited[break_cnt+1][ny][nx]:
#                         continue
#                     heappush(hq, [cnt+1, break_cnt+1, (nx, ny, n_is_morning)])
#                     visited[break_cnt][ny][nx] = 1
#                 else:
#                     heappush(hq, [cnt+1, break_cnt, (x, y, n_is_morning)])
#                     visited[break_cnt][y][x] = 1
#     return -1


# if __name__ == "__main__":
#     n,m,k = map(int, input().split())
#     board = [input() for _ in range(n)]
#     print(solve(n,m,k,board))

# import sys
# input = sys.stdin.readline

# from collections import deque

# dx = [-1,1,0,0]
# dy = [0,0,1,-1]
# def get_near(n,m,x,y):
#     for i in range(4):
#         nx, ny = x+dx[i], y+dy[i]
#         if 0<=nx<m and 0<=ny<n:
#             yield nx, ny

# def solve(n, m, k, board):
#     visited = [[[float("inf") for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
#     hq = deque()
#     hq.append([1,k,(0,0)])
#     visited[k][0][0]=0
    
#     while hq:
#         cnt, break_cnt, (x, y) = hq.popleft()
#         if x==m-1 and y==n-1:
#             return cnt
#         for nx, ny in get_near(n,m,x,y):
#             if board[ny][nx]=="0" and visited[break_cnt][ny][nx]>cnt:
#                 visited[break_cnt][ny][nx]=cnt
#                 hq.append([cnt+1, break_cnt, (nx,ny)])
#             else:
#                 if break_cnt and visited[break_cnt-1][ny][nx]>cnt:
#                     if cnt%2:
#                         visited[break_cnt-1][ny][nx] = cnt
#                         hq.append([cnt+1, break_cnt-1, (nx,ny)])
#                     else:
#                         hq.append([cnt+1, break_cnt, (x,y)])
#     return -1


# if __name__ == "__main__":
#     n,m,k = map(int, input().split())
#     board = [input() for _ in range(n)]
#     print(solve(n,m,k,board))

import sys
input = sys.stdin.readline

from heapq import heappop, heappush

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def get_near(n,m,x,y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            yield nx, ny

def solve(n, m, k, board):
    visited = [[[float("inf") for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
    hq = []
    hq.append([1,k,(0,0)])
    visited[k][0][0]=0
    while hq:
        cnt, break_cnt, (x, y) = heappop(hq)
        if x==m-1 and y==n-1:
            return cnt
        for nx, ny in get_near(n,m,x,y):
            if board[ny][nx]=="0" and visited[break_cnt][ny][nx]>cnt:
                visited[break_cnt][ny][nx]=cnt
                heappush(hq, [cnt+1, break_cnt, (nx,ny)])
            else:
                if break_cnt and visited[break_cnt-1][ny][nx]>cnt:
                    if cnt%2:
                        visited[break_cnt-1][ny][nx] = cnt
                        heappush(hq, [cnt+1, break_cnt-1, (nx,ny)])
                    else:   
                        heappush(hq, [cnt+1, break_cnt, (x,y)])
    return -1


if __name__ == "__main__":
    n,m,k = map(int, input().split())
    board = [input() for _ in range(n)]
    print(solve(n,m,k,board))