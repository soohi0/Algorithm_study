import math
from collections import deque

def press_string(before, cnt, pressed):
    if cnt == 1:
        pressed += before
    else:
        pressed += (str(cnt) + before)
    return pressed

def solution(s):
    answer = 2000
    if len(s) == 1:
        return 1
    #문자열 길이의 절반 이하 크기로 잘라야함
    slice_len = len(s)//2
    for i in range(1, slice_len+1, 1):
        sliced_list = []
        s_idx = 0
        while s_idx + i <= len(s) - 1:
            sliced_list.append(s[s_idx:s_idx+i])
            s_idx += i
        if s_idx < len(s):
            sliced_list.append(s[s_idx:])
        # print(sliced_list)
        pressed = ''
        before = ''
        cnt = 1
        q = deque(sliced_list)
        while q:
            if before == '':
                before = q.popleft()
            else:
                front = q.popleft()
                if front == before:
                    cnt += 1
                else:
                    pressed = press_string(before, cnt, pressed)
                    cnt = 1
                    before = front
        else:
            pressed = press_string(before, cnt, pressed)
        if answer > len(pressed):
            answer = len(pressed)
    
    return answer