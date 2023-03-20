from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses, speeds = deque(progresses), deque(speeds)

    while progresses:
        for idx in range(len(speeds)):
            progresses[idx] += speeds[idx]
            
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    
    return answer