import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
power_dict = defaultdict(list)
for _ in range(N):
    name, val = map(str, input().split())
    power_dict[int(val)].append(name)

power_list = list(power_dict.keys())

def binary_search(point):
    left, right = 0, len(power_list) - 1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if point <= power_list[mid]:
            result = mid
            right = mid - 1        
        else:
            left = mid + 1
    
    return power_dict[power_list[result]][0]

for _ in range(M):
    point = int(input())
    print(binary_search(point))