import sys
input = sys.stdin.readline

from bisect import bisect_left

class IFManager:
    def __init__(self, conditions):
        self.names, self.values = map(list,zip(*conditions))
    
    def __call__(self, n):
        print(self.names[bisect_left(self.values, n)])

if __name__=="__main__":
    n, m = map(int, input().split())
    conditions = list(map(lambda x:(x[0],int(x[1])), (input().split() for _ in range(n))))
    func = IFManager(conditions)
    for _ in range(m):
        func(int(input()))
        