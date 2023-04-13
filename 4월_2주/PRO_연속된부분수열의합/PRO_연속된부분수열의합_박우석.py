import heapq
def solution(seq, k):
    # 투포인터
    p1, p2 = 0, 0
    cand = []
    total = seq[0]
    while p1 <= p2:
        if total == k:
            heapq.heappush(cand, (p2-p1, [p1, p2]))
            # 뒤에 더 탐색
            p2 += 1
            if p2 < len(seq):
                total += seq[p2]
        elif total < k:
            # 뒤 탐색
            p2 += 1
            if p2 < len(seq):
                total += seq[p2]
        elif total > k:
            # 앞에서 당겨오기
            p1 += 1
            if p1 <= p2:
                total -= seq[p1-1]
        
        if p2 >= len(seq):
            break
        
    return heapq.heappop(cand)[1]