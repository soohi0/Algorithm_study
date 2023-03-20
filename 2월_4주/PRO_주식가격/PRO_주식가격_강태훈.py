import heapq

def solution(prices):
    answer = [0] * len(prices)
    pq = []
    
    for time, price in enumerate(prices):
        heapq.heappush(pq, (-price,time))
        while pq[0][0] < -price:
            value, input_time = heapq.heappop(pq)
            answer[input_time] = time-input_time
    while pq:
        value, input_time = heapq.heappop(pq)
        answer[input_time] = time-input_time
    return answer