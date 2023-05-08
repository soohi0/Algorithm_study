def solution(sequence):
    n = len(sequence)
    sum_list = [0] * n
    if n == 1:
        return abs(sequence[0])
    
    sum_list[0] = sequence[0] * -1
    min_val, max_val = sum_list[0], sum_list[0]
    
    for idx in range(1, n):
        if idx % 2:
            val = sum_list[idx-1] + sequence[idx] 
        else:
            val = sum_list[idx-1] + sequence[idx] * -1
            
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
            
        sum_list[idx] = val
    
    # print(sum_list)
    # print(max_val, min_val)
    return max(abs(max_val - min_val), max_val, abs(min_val))