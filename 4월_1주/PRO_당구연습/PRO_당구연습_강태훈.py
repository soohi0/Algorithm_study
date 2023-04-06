def one(m, n, x, y):
    _x, _y = m-x, n-y
    return [(-x,y), (x,-y), (x+2*_x,y), (x,y+2*_y)]

def distance(loc1, loc2):
    return sum([(i-j)**2 for i, j in zip(loc1, loc2)])

def solution(m, n, startX, startY, balls):
    coords = one(m, n, startX, startY)
    global_answer = []
    for ball in balls:
        ball_x, ball_y = ball
        answer = float("inf")
        for new in coords:
            new_x, new_y = new
            if min(new_x, startX) <= ball_x <= max(new_x, startX) and new_y==ball_y==startY:
                continue
            elif min(new_y, startY) <= ball_y <= max(new_y, startY) and new_x==ball_x==startX:
                continue
            else:
                answer = min(answer, distance(new, ball))
        global_answer.append(answer)
    return global_answer