def solution(prices):
    answer = [0] * (len(prices))
    # 2중 for문
    for idx_1 in range(len(prices)):
        for idx_2 in range(idx_1+1, len(prices)):
            if prices[idx_1] > prices[idx_2]:
                answer[idx_1] = idx_2 - idx_1
                break
        else:
            answer[idx_1] = len(prices) - 1 - idx_1
    
    return answer