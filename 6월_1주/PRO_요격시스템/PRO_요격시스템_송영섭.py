def solution(targets):
    n = len(targets)
    targets.sort(key=lambda x: x[1])

    cs, ce = targets[0]
    cnt = 1
    for i in range(1, n):
        ns, ne = targets[i]
        if ns >= ce:
            cnt += 1
            cs, ce = ns, ne
        
    return cnt