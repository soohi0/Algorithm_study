import itertools
def solution(k, dungeons):
    answer = -1
    idxs = [i for i in range(len(dungeons))]
    
    for idx_order in itertools.permutations(idxs):
        li = list(idx_order)
        k_ = k
        cnt = 0
        for idx in idx_order:
            if dungeons[idx][0] <= k_:
                k_ -= dungeons[idx][1]
                cnt += 1
        if answer < cnt:
            answer = cnt
            
    return answer