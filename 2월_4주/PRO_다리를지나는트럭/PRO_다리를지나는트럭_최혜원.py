from collections import deque
def solution(bridge_length, weight, truck_weights):
    timestep = 0
    
    moving = deque([]) #다리를 건너는 중인 트럭들 dq
    moved_cnt = 0 #다리를 이미 지난 트럭개수
    length = len(truck_weights) #초기 대기 트럭 개수, while문 조건 위함
    weight_sum = 0 #다리를 건너는 중인 트럭 무게. sum을 사용하면 시간이 오래걸림
    
    while moved_cnt != length:
        if len(moving) >= bridge_length:
            if len(moving) >= bridge_length:
                re = moving.popleft()
                weight_sum -= re
                if re != 0:
                    moved_cnt += 1
        if len(moving) < bridge_length and len(truck_weights) >= 0:
            if len(truck_weights) > 0:
                front = truck_weights[0]
                if (weight_sum + front) <= weight:
                    #총 무게가 미달이면 넣을 수 있다.
                    moving.append(front)
                    weight_sum += front
                    truck_weights = truck_weights[1:]
                else:
                    #무게는 미달이어도 지나가는 트럭 개수가 다리 전체길이보다 모자르면 0채움
                    moving.append(0)
            else:                     
                moving.append(0)
        timestep += 1

    return timestep