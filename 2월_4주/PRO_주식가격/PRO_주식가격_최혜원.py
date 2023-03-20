# *****런타임에러..*************
from collections import deque

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = deque([]) #증가중인 애들 (cnt, idx)
    pre_price = 0
    for idx, price in enumerate(prices):
        #감소할 경우 -> popleft
        if price < pre_price:
            for st_idx in range(len(stack)):
                elem = stack[st_idx]
                if prices[elem[1]] > price:
                    answer[elem[1]] = elem[0]
                    stack.remove(elem)
        if stack:
            for st_idx in range(len(stack)):
                stack[st_idx][0] += 1
        stack.append([1, idx])
        pre_price = price

    for st in stack:
        answer[st[1]] = st[0]-1
    answer[-1] = 0
    
    
    return answer