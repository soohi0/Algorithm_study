import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1,0,1,0]
dy = [0,1,0,-1]
n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 1
board[x][y] = 2

def solve(n,m,x,y,d,flag=0):
    global cnt
    if flag == 4:
        move_d = (d+2)%4
        nx, ny = x+dx[move_d], y+dy[move_d]
        if board[nx][ny] == 1:
            return
        else:
            board[nx][ny] = 2
            solve(n,m,nx,ny,d,0)
    else:
        move_d = (d+3)%4
        nx, ny = x+dx[move_d], y+dy[move_d]
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            cnt += 1
            solve(n,m,nx,ny,move_d,0)
        else:
            solve(n,m,x,y,move_d,flag+1)


solve(n, m, x, y, d, 0)
print(cnt)