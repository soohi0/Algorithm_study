import sys
from heapq import heappop, heappush
from bisect import bisect_left

input = lambda : sys.stdin.readline()

n, m = map(int, input().split())


chingho = list(map(lambda x: (x[0], int(x[1])),[input().split() for _ in range(n)])) #길이 100000
powers = [int(input()) for _ in range(m)] #길이 100000
chingho_nums = list(map(lambda x: x[1], chingho))

#길이가 짧고 정렬되어있으니까 이분탐색 의심!
for power in powers:
    idx = bisect_left(chingho_nums, power)
    print(chingho[idx][0])



# powers = []
# for idx in range(m):
#     power = int(input().strip())
#     heappush(powers, [power, idx])

# answer = ['' for _ in range(m)]
# for b, n in chingho:
#     if len(powers) <= 0:
#         break
#     if powers[0][0] > b:
#         continue
#     while powers[0][0] <= b:
#         power, idx = heappop(powers)
#         answer[idx] = n
#         if len(powers) <= 0:
#             break
# print(*answer)

