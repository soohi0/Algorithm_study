from collections import deque

def solution(bridge_length, weight, truck_weights):
    cross = deque()
    truck_weights = deque(truck_weights)
    time, w = 0, 0
    
    while truck_weights or cross:
        time += 1
        if cross and time-cross[0][1] >= bridge_length:
            w -= cross[0][0]
            cross.popleft()
        if truck_weights and truck_weights[0] + w <= weight:
            cross.append((truck_weights.popleft(),time))
            w += cross[-1][0]
    return time