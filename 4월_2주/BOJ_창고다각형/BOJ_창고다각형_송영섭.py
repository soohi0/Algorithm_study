import sys
from collections import defaultdict
sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

N = int(input())

# 기둥 dict 생성 : {key=위치 : value=높이}
pillow_dict = defaultdict(int)
for _ in range(N):
    L, H = map(int, input().split())
    pillow_dict[L] = H

pillow_list = list(pillow_dict.keys())
pillow_list.sort()

left, right = pillow_list[0], pillow_list[-1]
left_h, right_h = 0, 0
max_h = max(list(pillow_dict.values())) # 가장높은 기둥 값
box = 0
while left_h < max_h or right_h < max_h:
    # 더 높은 기둥 높이가 있으면 갱신
    if pillow_dict[left] and pillow_dict[left] > left_h:
        left_h = pillow_dict[left]
    if pillow_dict[right] and pillow_dict[right] > right_h:
        right_h = pillow_dict[right]

    # max_h 보다 작으면 넓이에 높이값 더함
    if left_h < max_h: 
        left += 1
        box += left_h
    if right_h < max_h:
        right -= 1
        box += right_h 

# 가장 높은 직사각형 더함
box += (right - left + 1) * max_h

print(box)