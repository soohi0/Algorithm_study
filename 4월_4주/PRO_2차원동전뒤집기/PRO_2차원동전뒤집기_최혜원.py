from collections import deque
def change(beginning, idx,colorrow):
    if colorrow: #True: col
        for c_idx, begin in enumerate(beginning):
            if beginning[c_idx][idx] == 1:
                beginning[c_idx][idx] = 0
            else:
                beginning[c_idx][idx] = 1
    else:
        for r_idx, begin in enumerate(beginning[idx]):
            if beginning[idx][r_idx] == 1:
                beginning[idx][r_idx] = 0
            else:
                beginning[idx][r_idx] = 1     
def solution(beginning, target):
    answer = -1
    cnt = 0
    
    # 행 -> 열[1:] -> 행[1:] -> 열 ->
    sero, garo = len(beginning), len(beginning[0])

    length = max(sero, garo)
        
    for idx in range(length):
        #idx 열 탐색 후 어떤 행을 바꿔야할지 선택
        if idx < sero:
            for_change = deque([])
            for l_idx in range(idx, sero, 1):
                if target[l_idx][idx] != beginning[l_idx][idx]:
                    for_change.append(l_idx)
            while for_change:
                change_idx = for_change.popleft()
                change(beginning, change_idx, False)
                cnt += 1
        # for b in beginning:
        #     print(b)
        # print('----------')
                if beginning == target:
                    return cnt
        if idx+1 < garo:
            for_change2 = deque([])
            for c_idx in range(idx+1, garo, 1):
                # print(c_idx, idx)
                if target[idx][c_idx] != beginning[idx][c_idx]:
                    for_change2.append(c_idx)
            
            while for_change2:
                change_idx = for_change2.popleft()
                change(beginning, change_idx, True)
                cnt += 1

#         for b in beginning:
#             print(b)
#         print('----------')
                if beginning == target:
                    return cnt
    
    return answer