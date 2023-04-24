def solution(x, y, n):
    # 다이나믹?
    if x == y:
        return 0
    
    dy = []
    dy.append(set([x + n, x * 2, x * 3]))
    cnt = 1
    while True:
        if y in dy[-1]:
            return cnt
        
        if all(val > y for val in dy[-1]):
            return -1
        
        tmp = set()
        for val in dy[-1]:
            x1 = val + n
            x2 = val * 2
            x3 = val * 3
            tmp.add(x1)
            tmp.add(x2)
            tmp.add(x3)
        
        dy.append(tmp)
        cnt += 1
