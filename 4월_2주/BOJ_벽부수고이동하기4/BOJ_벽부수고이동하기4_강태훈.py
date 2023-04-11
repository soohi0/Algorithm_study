import sys
from collections import deque

input = lambda : sys.stdin.readline().strip()

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def get_near(n, m, loc):
    for i in range(4):
        nx, ny = loc[0]+dx[i], loc[1]+dy[i]
        if 0<=nx<m and 0<=ny<n:
            yield nx, ny

def solve(n, m, board):
    group_cnt = {}
    group_idx = 0
    grouped_board = [[0]*m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if board[y][x] == "1":
                continue
            if grouped_board[y][x]>1:
                continue
            group_idx += 1
            local_group = set([(x,y)])
            q = deque([(x,y)])
            while q:
                cloc = q.popleft()
                for nloc in get_near(n, m, cloc):
                    nx, ny = nloc
                    if (nloc not in local_group) and (board[ny][nx]=="0"):
                        local_group.add(nloc)
                        q.append(nloc)
            group_cnt[group_idx] = len(local_group)
            for nx, ny in local_group:
                grouped_board[ny][nx] = group_idx

    answer = []
    for y in range(n):
        line = ""
        for x in range(m):
            if board[y][x] == "0":
                line += "0"
            else:
                near_groups = set()
                for nx, ny in get_near(n,m,(x,y)):
                    near_groups.add(grouped_board[ny][nx])
                sumval = 1
                for group_name in filter(lambda x:x, near_groups):
                    sumval = (group_cnt[group_name]+sumval)%10
                line += str(sumval%10)
        answer.append(line)
    return answer

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    print(*solve(n,m,board), sep="\n")