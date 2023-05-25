import sys  
input = lambda : sys.stdin.readline().strip()
N = int(input())

# # 480 -> 408 : 비트 연산으로 2의 배수 제거 
# a = [i&1 for i in range(N+1)]
# a[1] = 0
# # 640 -> 480 : 원소 -> 원소 제곱근
# for i in range(3, int(N**0.5)+1, 2):
#     if a[i]:
#         # 408 -> 392 : i의 2 배수부터 탐색 -> i의 제곱부터 탐색
#         for j in range(i*i, N+1, i):
#             a[j] = 0

# sosu_list = [2]
# for i in range(N+1):
#     if a[i] == True:
#         sosu_list.append(i)

# answer, temp, e = 0, 0, 0
# for i in range(len(sosu_list)):
#     while temp<N and e<len(sosu_list):
#         # 1600 -> 772 : sum -> 원소 누적 합
#         temp += sosu_list[e]
#         e += 1
#     if temp==N:
#         answer += 1
#     # 772 -> 640 : temp 다시 계산 -> 투포인터
#     temp -= sosu_list[i]

# 408 -> 208 : 비트마스킹 
a = [255 for _ in range(N//8 +1)]

def is_prime(n):
    return True if a[n>>3] & (1<<(n&7)) else False

def set_composite(n):
    a[n>>3] &= ~(1 << (n&7))

set_composite(0)
set_composite(1)

for i in range(2, int(N**(1/2))+1):
    if is_prime(i):
        for j in range(i*i, N+1, i):
            set_composite(j)

sosu_list = list()
for i,sosu in enumerate(a):
    for j in range(8):
        if sosu & (1 << j) and i*8+j <= N:
            sosu_list.append(i*8+j)

answer, temp, e = 0, 0, 0
for i in range(len(sosu_list)):
    while temp<N and e<len(sosu_list):
        temp += sosu_list[e]
        e += 1
    if temp==N:
        answer += 1
    temp -= sosu_list[i]

print(answer)