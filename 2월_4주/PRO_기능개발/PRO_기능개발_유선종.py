from collections import deque

def solution(progresses, speeds):
    q = deque([])
    for pbar, s in zip(progresses, speeds):
        dates, remain = divmod((100 - pbar), s)
        if remain:
            dates += 1
        q.append(dates)
    
    answer = []
    while q:
        complete = q.popleft()
        cnt = 1
        while q:
            if q[0] <= complete:
                q.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)
    
    return answer