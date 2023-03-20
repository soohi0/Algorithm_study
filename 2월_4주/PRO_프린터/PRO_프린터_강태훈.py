from collections import deque

def solution(priorities, location):
    task = deque(enumerate(priorities))
    answer = 0
    while task:
        curr = task.popleft()
        if task and max(list(zip(*task))[1]) > curr[1]:
            task.append(curr)
        else:
            answer += 1
            if curr[0] == location:
                return answer