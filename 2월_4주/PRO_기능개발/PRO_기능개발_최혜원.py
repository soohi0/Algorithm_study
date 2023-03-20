import math
def solution(progresses, speeds):
    answer = []
    completes = []
    
    for idx, progress in enumerate(progresses):
        rest = math.ceil((100 - progress) / speeds[idx])
        completes.append(rest)
        
    pre_com = completes[0]
    pre_cnt = 1
    if len(completes) > 1:
        for c_idx in range(1, len(completes)):
            if completes[c_idx] <= pre_com:
                pre_cnt += 1
            else:
                answer.append(pre_cnt)
                pre_cnt = 1
                pre_com = completes[c_idx]
                    
    answer.append(pre_cnt)
    
    return answer