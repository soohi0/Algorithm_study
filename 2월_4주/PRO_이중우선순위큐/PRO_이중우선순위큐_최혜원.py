import heapq
def solution(operations):
    hq = []
    
    for operation in operations:
        text, num = operation.split(' ')
        num = int(num)
        if text == 'I':
            heapq.heappush(hq, num)
        elif text == 'D':
            try:
                if num == -1:
                    heapq.heappop(hq)
                elif num == 1:
                    hq = hq[:-1]
            except:
                pass
        # print(hq)       
    hq = sorted(hq)
    if hq:
        return [hq[-1], hq[0]]
    else:
        return [0,0]