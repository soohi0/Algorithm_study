from collections import defaultdict

def solution(weights):
    n = len(weights)
    count_weight = defaultdict(int)
    for i in weights:
        count_weight[i] += 1
    
    result = 0
    for key in count_weight.keys():
        val = count_weight[key]
        if val > 1:
            result += val * (val-1) / 2 # nCr 계산
        if key * (3/2) in count_weight:
            result += val * count_weight[key * (3/2)]
        if key * (4/3) in count_weight:
            result += val * count_weight[key * (4/3)]
        if key * 2 in count_weight:
            result += val * count_weight[key * 2]
            
    return result