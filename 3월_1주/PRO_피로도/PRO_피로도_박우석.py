from itertools import permutations
def solution(k, dungeons):
    comb = permutations(dungeons, len(dungeons))
    # 한 조합 당 탐험 가능한지 확인
    max_dun = 0
    for seq in comb:
        user_k = k
        dun_count = 0
        for need, cost in seq:
            if user_k >= need:
                user_k -= cost
                dun_count += 1
            else: break
        
        if max_dun < dun_count:
            max_dun = dun_count
        
    return max_dun