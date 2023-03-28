def solution(stones, k):
    s, e = 1, 200000000
    while s <= e:
        m = (s + e) // 2
        if any([len(j)>=k for j in "".join(["1" if i<=m else " " for i in stones]).split()]):
            e = m-1
        else:
            s = m+1
    return s