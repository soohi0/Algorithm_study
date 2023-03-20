from collections import deque
def isinRange(x, y, garo, sero):
    if x < garo and x >= 0 and y < sero and y >= 0:
        return True
    else:
        return False
    
def solution(maps):

    answer = -1
    garo = len(maps[0])
    sero = len(maps)
    
    q = deque([[0, 0, 1]])
    dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while q:
        front = q.popleft()
        X, Y, dist = front
        if Y == sero-1 and X == garo-1 :
            return dist
        for x, y in dirs:
            newX = X + x
            newY = Y + y
            if isinRange(newX, newY, garo, sero):
                if maps[newY][newX] == 1:
                    #go
                    q.append([newX, newY, dist+1])
                    maps[newY][newX] = -1
                    
    return answer