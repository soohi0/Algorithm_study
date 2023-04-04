from collections import deque
def isitRange(x, y, garo, sero):
    if x < garo and x >= 0 and y < sero and y >= 0:
        return True
    return False
def solution(board):
    answer = -1
    R = [] #y, x, 0
    G = []
    visited = []
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    #find R, D
    for y_idx, line in enumerate(board):
        visit = []
        for x_idx, s in enumerate(line):
            if s == 'R':
                R.append(y_idx)
                R.append(x_idx)
                visit.append(0)
            elif s == 'G':
                G.append(y_idx)
                G.append(x_idx)
                visit.append(0)
            elif s == '.':
                visit.append(0)
            elif s == 'D':
                visit.append(-1)
        visited.append(visit)
    q = deque([R+[1]])
    visited[R[0]][R[1]] = 1
    while q:
        spot_y, spot_x, cnt = q.popleft()
        next_x , next_y = spot_x, spot_y
        if [spot_y, spot_x] == G:
            answer = cnt
            break
        for x, y in dirs:
            ischange = False
            next_x , next_y = spot_x, spot_y
            print(spot_x, spot_y, x, y)
            while isitRange(next_x+x, next_y+y, len(board[0]), len(board)):
                if visited[next_y+y][next_x+x] == -1:
                    break
                else:
                    next_x += x
                    next_y += y
                    ischange = True
            print(next_x, next_y, ischange)
            if ischange and visited[next_y][next_x] == 0:
                q.append([next_y, next_x, cnt+1])
                visited[next_y][next_x] = cnt+1
                for l in visited:
                    print(l)
                print('---------------')

        # break
    print(answer-1)
    return answer
solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])