def solution(m, n, startX, startY, balls):
    result = []
    for targetX, targetY in balls:
        tmp_list = []
        if not (startX == targetX and startY > targetY):
            cal_1 = (startX-targetX)**2 + (startY+targetY)**2
            tmp_list.append(cal_1)
        if not (startX == targetX and startY < targetY):
            cal_2 = (startX-targetX)**2 + ((n-startY)+(n-targetY))**2
            tmp_list.append(cal_2)
        if not (startY == targetY and startX > targetX):
            cal_3 = (startX+targetX)**2 + (startY-targetY)**2
            tmp_list.append(cal_3)
        if not (startY == targetY and startX < targetX):
            cal_4 = ((m-startX)+(m-targetX))**2 + (startY-targetY)**2
            tmp_list.append(cal_4)
        result.append(min(tmp_list))

    return result