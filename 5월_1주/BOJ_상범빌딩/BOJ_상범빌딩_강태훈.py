import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

dx = (0,0,1,-1,0,0)
dy = (1,-1,0,0,0,0)
dz = (0,0,0,0,1,-1)

def get_near(x, y, z, n, m, h):
    for i in range(6):
        nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
        if 0<=nx<m and 0<=ny<n and 0<=nz<h:
            yield nx, ny, nz

def escape(h, n, m ,building, s, e):
    q = deque()
    visited = [[[False]*m for _ in range(n)] for _ in range(h)]
    x, y, z = s
    visited[z][y][x] = True
    q.append([s, 0])
    while q:
        (cx, cy, cz), cnt = q.popleft()
        for nx, ny, nz in get_near(cx, cy, cz, n, m, h):
            if visited[nz][ny][nx]:
                continue
            if (nx,ny,nz) == e:
                print(f"Escaped in {cnt+1} minute(s).")
                return
            if building[nz][ny][nx] == "#":
                continue
            visited[nz][ny][nx] = True
            q.append([(nx, ny, nz), cnt+1])
    print("Trapped!")
    return

if __name__ == "__main__":
    while True:
        h, n, m = map(int, input().split())
        if h == n == m == 0:
            break
        s, e = None, None
        building = []
        for z in range(h):
            board = []
            for y in range(n):
                line = input()
                for x in range(m):
                    if line[x]=="S":
                        s = (x,y,z)
                    elif line[x]=="E":
                        e = (x,y,z)
                board.append(line)
            building.append(board)
            input()
        escape(h, n, m, building, s, e)