def solution(sizes):
    answer = 0
    max_garo = 0
    max_sero = 0
    
    for size in sizes:
        garo, sero = size
        mid_garo1 = max_garo
        mid_sero1 = max_sero
        mid_garo2 = max_garo
        mid_sero2 = max_sero
        
        if mid_garo1 < garo:
            mid_garo1 = garo
        if mid_sero1 < sero:
            mid_sero1 = sero
        if mid_garo2 < sero:
            mid_garo2 = sero
        if mid_sero2 < garo:
            mid_sero2 = garo
        if mid_garo1 * mid_sero1 < mid_garo2 * mid_sero2:
            max_garo = mid_garo1
            max_sero = mid_sero1
        else:
            max_garo = mid_garo2
            max_sero = mid_sero2
        # print(max_garo, max_sero)
        
    
    return max_garo * max_sero