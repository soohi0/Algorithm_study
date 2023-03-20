import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    min_k = scoville[0]
    while min_k < K:
        try:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
        except:
            return -1
        new = first + second * 2
        heapq.heappush(scoville, new)
        min_k = scoville[0]
        answer += 1
    
    return answer