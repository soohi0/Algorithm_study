import numpy as np
    
def solution(m, n, startX, startY, balls):
    answer = []
    for bX, bY in balls:
        temp = []
        # 왼쪽 벽
        if not (startX>=bX and startY==bY):
            temp.append((startX+bX)**2 + (startY-bY)**2)
        # 위쪽 벽
        if not (startX==bX and startY<=bY):
            temp.append((startX-bX)**2 + ((n-startY)+(n-bY))**2)
        # 오른쪽 벽
        if not (startX<=bX and startY==bY):
            temp.append(((m-startX)+(m-bX))**2 + (startY-bY)**2)
        # 아래쪽 벽
        if not (startX==bX and startY>=bY):
            temp.append((startX-bX)**2 + (startY+bY)**2)
        answer.append(min(temp))
    return answer 
            