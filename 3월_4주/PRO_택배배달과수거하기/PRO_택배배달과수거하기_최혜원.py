from collections import deque
def solution(cap, n, deliveries, pickups):
    answer = 0
    #greedy로 제일 멀리있는 것부터 처리해보자
    d_stack = deque(deliveries)
    p_stack = deque(pickups)
    if sum(d_stack) + sum(p_stack) == 0:
        return 0
    while d_stack or p_stack:
        # print(d_stack, p_stack)
        pack = 0
        d_max_distance = 0
        while d_stack:
            if pack + d_stack[-1] <= cap:
                pack += d_stack[-1]
                if d_max_distance < len(d_stack):
                    d_max_distance = len(d_stack)
                d_stack.pop()
            else:
                d_stack[-1] -= (cap-pack)
                if d_max_distance < len(d_stack):
                    d_max_distance = len(d_stack)
                break
        pack = 0
        p_max_distance = 0
        while p_stack:
            # print(p_stack)
            if pack + p_stack[-1] <= cap:
                pack += p_stack[-1]
                if p_max_distance < len(p_stack):
                    p_max_distance = len(p_stack)
                p_stack.pop()
            else:
                p_stack[-1] -= (cap-pack)
                if p_max_distance < len(p_stack):
                    p_max_distance = len(p_stack)
                break
        # print(d_max_distance, p_max_distance)
        # print(d_stack, p_stack)
        # print('-------------------')
        
        answer += (max(p_max_distance, d_max_distance))*2
                
        
    return answer