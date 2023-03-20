from collections import deque

def solution(bridge_length, weight, truck_weights):
    # bridge_que, time_que, truck_que
    b_que, time_que, truck_que = deque(), deque(), deque(truck_weights)
    
    # while
    time = 0
    while b_que or truck_que:
        # 다리에서 벗어난 트럭 que 에서 빼기
        if time_que:
            for idx, val in enumerate(time_que):
                time_que[idx] += 1
            if time_que[0] == bridge_length:
                b_que.popleft()
                time_que.popleft()
                
        # 다리에 트럭 올리기
        if truck_que and len(time_que) < bridge_length and sum(b_que) + truck_que[0] <= weight:
            b_que.append(truck_que.popleft())
            time_que.append(0)
        time += 1
            
    return time