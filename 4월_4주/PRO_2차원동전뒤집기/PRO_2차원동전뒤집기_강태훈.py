from heapq import heappush, heappop

def transform(n, m, ns, ms):
    init_val = int(ms, 2)
    return [(((1<<m)-1)*int(tok))^init_val for tok in ns]

def get_case(n, m):
    hq = []
    for i in range(2**(n+m)-1):
        cmd = format(i, "b").zfill(n+m)
        heappush(hq, [cmd.count("1"), cmd])
    while hq:
        cnt, case = heappop(hq)
        yield cnt, transform(n, m, case[:n], case[n:])
    
def solution(beginning, target):
    val = [int("".join(map(str,i)),2)^int("".join(map(str,j)),2) for i, j in zip(beginning, target)]
    for cnt, cmd in get_case(len(beginning), len(beginning[0])):
        if val == cmd:
            return cnt
    return -1