from collections import deque
def solution(priorities, location):
    answer = 0
    length = len(priorities)
    
    to_prints = [False for _ in range(length)]
    to_prints[location] = True
    pri_check = sorted(priorities, reverse=True)
    
    dq = deque(priorities)
    p_dq = deque(to_prints)
    while len(dq) > 0:
        front = dq.popleft()
        p_front = p_dq.popleft()
        if front != pri_check[0]:
            dq.append(front)
            p_dq.append(p_front)
        else:
            answer += 1
            pri_check = pri_check[1:]
            if p_front == True:
                return answer

    return answer