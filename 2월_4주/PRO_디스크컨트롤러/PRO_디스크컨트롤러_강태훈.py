from heapq import heapify, heappush, heappop

def solution(jobs):
    heapify(jobs)
    disk = []
    answer, current_time, maxlen = 0, 0, len(jobs)
    
    while jobs or disk:
        while jobs and jobs[0][0] <= current_time:
            heappush(disk, list(reversed(heappop(jobs))))
        
        if disk:
            req_time, init_time = heappop(disk)
            current_time += req_time
            answer += (current_time - init_time)
        else:
            current_time += 1
    return int(answer/maxlen)