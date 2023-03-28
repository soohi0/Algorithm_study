import heapq as hq

def solution(stones, k):
    que = [(-val, idx) for idx, val in enumerate(stones[ :k])]
    hq.heapify(que)
    max_val = -que[0][0]
    min_max_que = max_val
    
    for idx in range(k, len(stones)):
        append_val = stones[idx]
        hq.heappush(que, (-append_val, idx))
        
        while que[0][1] <= idx - k: # 최대값 인덱스가 슬라이딩 윈도우 범위를 벗어나면 계속 pop
            hq.heappop(que)
            
        max_val = -que[0][0]

        if max_val < min_max_que:
            min_max_que = max_val
    
    return min_max_que