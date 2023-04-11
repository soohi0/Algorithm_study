import sys
input = sys.stdin.readline

from collections import defaultdict, deque

n, m = map(int, input().split(' '))

employ_input = list(map(int, input().split(' ')))
connection = defaultdict(list)
for idx, val in enumerate(employ_input):
    connection[val].append(idx+1)

praise_dict = defaultdict(int)
for _ in range(m):
    i, w = map(int, input().split())
    praise_dict[i] += w

sum_list = [0] * (len(employ_input) + 1)

que = deque()
que.append(-1)

while que:
    employ = que.popleft()
    if praise_dict[employ]:
        sum_list[employ] += praise_dict[employ]

    for junior in connection[employ]:
        sum_list[junior] += sum_list[employ]
        que.append(junior)

print(*sum_list[1:])