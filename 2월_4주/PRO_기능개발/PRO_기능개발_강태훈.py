from math import ceil

def solution(progresses, speeds):
    day = 0
    answer = []
    for progress, speed in zip(progresses, speeds):
        c_progress = day * speed + progress
        if c_progress >= 100:
            answer[-1] += 1
        else:
            day += ceil((100-c_progress)/speed)
            answer.append(1)
    return answer