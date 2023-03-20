import math
from collections import deque
def solution(arr):
    answer_st = []
    answer_en = deque([])
    #two pointer 사용
    pre_st_idx = arr[0]
    pre_en_idx = arr[-1]
    
    for idx in range(len(arr)//2):
        if arr[idx] != pre_st_idx:
            answer_st.append(pre_st_idx)
            pre_st_idx = arr[idx]
        if arr[-(idx+1)] != pre_en_idx:
            answer_en.appendleft(pre_en_idx)
            pre_en_idx = arr[-(idx+1)]
            
    if len(arr) % 2 == 1:
        idx = math.ceil(len(arr)/2)-1
        answer_st.append(pre_st_idx)
        if arr[idx] != pre_en_idx and arr[idx] != pre_st_idx:
            answer_st.append(arr[idx])
            answer_en.appendleft(pre_en_idx)
        elif arr[idx] != pre_st_idx or arr[idx] != pre_en_idx:
            answer_en.appendleft(pre_en_idx)
    else:
        answer_st.append(pre_st_idx)  
        if pre_st_idx != pre_en_idx:
            answer_en.appendleft(pre_en_idx)
        
            
    
    return answer_st + list(answer_en)