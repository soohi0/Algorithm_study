import sys
input = sys.stdin.readline

def check(nums, v, k, cumsum=0, init_group=0):
    for n in nums:
        cumsum += n
        if cumsum>=v:
            init_group+=1
            cumsum=0
            if init_group >= k:
                return True
    return False

def solution(nums, k):
    s, e = 0, 20*n//k+1
    while s<e:
        m = (s+e)//2
        if check(nums, m, k): # Impossible
            s = m+1
        else: # Possible
            e = m
    return s-1

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solution(list(map(int, input().split())), k))