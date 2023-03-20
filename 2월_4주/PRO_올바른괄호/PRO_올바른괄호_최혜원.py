from collections import deque
def solution(s):
    answer = True
    
    dq = deque()
    for ss in s:
        if ss == '(':
            dq.append(ss)
        else:
            try:
                dq.popleft()
            except:
                answer = False
    if len(dq) != 0:
        answer = False

    return answer