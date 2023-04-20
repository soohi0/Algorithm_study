from heapq import heappush, heappop

def transform(ns, ms):
    init_val = int(ms, 2)
    for tok in ns:
        yield (((1<<len(ms))-1)*int(tok))^init_val

def get_case(n, m):
    hq = []
    for i in range(2**(n+m)):
        cmd = format(i, "b").zfill(n+m)
        heappush(hq, [cmd.count("1"), cmd])
    while hq:
        cnt, case = heappop(hq)
        yield cnt, transform(case[:n], case[n:])
    
def solution(beginning, target):
    n, m = len(beginning), len(beginning[0])
    beginning = [int("".join(map(str,x)),2) for x in beginning]
    target = [int("".join(map(str,x)),2) for x in target]
    val = tuple([i^j for i, j in zip(beginning, target)])
    for cnt, cmd in get_case(n, m):
        cmd = tuple(cmd)
        if val == cmd:
            return cnt
    return -1
