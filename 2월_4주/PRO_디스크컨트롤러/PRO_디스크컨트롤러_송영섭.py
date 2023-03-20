import heapq as hq

def solution(jobs):
    n = len(jobs)
    jobs.sort(reverse=True)
    heap_list = []
    
    time, sum_time, working = 0, 0, 0
    while heap_list or jobs:
        while jobs and jobs[-1][0] == time:
            tmp = jobs.pop()
            hq.heappush(heap_list, (tmp[1], tmp[0]))
        
        if heap_list and working == 0:
            a, b = hq.heappop(heap_list)
            sum_time += (time + a - b)
            working = a
        
        if working > 0:
            working -= 1
        time += 1
    
    return sum_time // n