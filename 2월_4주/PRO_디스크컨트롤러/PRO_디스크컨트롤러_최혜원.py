#greedy 로 풀어보자
#heapq 로 풀어보자
import heapq

def solution(jobs):
    answer = 0
    length = len(jobs)
    heapq.heapify(jobs)
    # print(jobs)
    curtime = 0
    while jobs:
        cando = []
        for job in jobs:
            if job[0] <= curtime:
                cando.append([job[1], job[0]])
        heapq.heapify(cando)
        # print(cando)
        if cando:
            answer += (curtime + cando[0][0] - cando[0][1])
            curtime += cando[0][0]
            jobs.remove([cando[0][1], cando[0][0]])
        else:
            front = heapq.heappop(jobs)
            # print(front)
            answer += front[1]
            curtime = (front[0] + front[1])
    return answer // length