from collections import deque

def solution(priorities, location):
    # 작업 중요도 리스트
    location_list = [0] * len(priorities)
    location_list[location] = 1
    
    # deque
    p_que, l_que = deque(priorities), deque(location_list)
    # print(p_que, l_que)
    
    # for + pop
    cnt = 0
    while p_que:
        if p_que[0] == max(p_que):
            cnt += 1
            # 조건일 때
            if l_que[0] == 1:
                return cnt
            p_que.popleft()
            l_que.popleft()

        else:
            p_que.append(p_que.popleft())
            l_que.append(l_que.popleft())