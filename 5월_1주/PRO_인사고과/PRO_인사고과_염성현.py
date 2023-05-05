def solution(scores):
    answer = 1
    wan_x, wan_y = scores[0][0], scores[0][1]
    scores.sort(key=lambda x:(-x[0], x[1]))
    tmp = 0
    for others_x, others_y in scores:
        if wan_x < others_x and wan_y < others_y:
            return -1
        if wan_x+wan_y < others_x+others_y and tmp <= others_y:
            answer += 1        
            tmp = others_y
    return answer