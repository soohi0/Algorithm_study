from typing import *
from heapq import heappush, heappop

def solution(prices:List[int]) -> List[int]:
    answer:List[int] = [0] * len(prices)
    hq:List[Tuple[int]] = []
    for c_i, c_price in enumerate(prices):
        heappush(hq,(-c_price, c_i))
        if hq[0][0] * (-1) > c_price:
            while hq:
                p_price, p_i = heappop(hq)
                
                if p_price * (-1) <= c_price:
                    heappush(hq, (p_price, p_i))
                    break
                    
                answer[p_i] = c_i - p_i
            max_value = hq[0][0] * (-1)
            
    while hq:
        p_price, p_i = heappop(hq)
        answer[p_i] = (len(prices)-1) - p_i

    return answer