def solution(sequence, k):
    s = e = 0
    answer = [0,float("inf")]
    maxidx, sumval = len(sequence)-1, sequence[s]
    
    while s<maxidx+1 and e<maxidx+1:
        if sumval==k:
            answer = [s,e] if e-s<answer[1]-answer[0] else answer
        if e==maxidx and sumval<=k:
            break
        (s,e,sumval) = (s,e+1,sumval+sequence[e+1]) if sumval<k and e<maxidx else (s+1,e,sumval-sequence[s])
    return answer