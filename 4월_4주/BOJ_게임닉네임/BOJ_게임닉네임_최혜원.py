import sys
from collections import defaultdict, deque
input = lambda : sys.stdin.readline()

def same_part(name1, name2):
    length = 0
    if len(name1) > len(name2):
        length = len(name2)
    else:
        length = len(name1)
    for l in range(length):
        if name1[l] != name2[l]:
            return l
    return length

n = int(input())

names = [input().strip() for _ in range(n)]
name_dict = defaultdict(dict) #{pre: {name:cnt}}

for name in names:
    flag = False
    q = deque([])
    for prefix_len in range(1, len(name)+1, 1):
        prefix = name[0:prefix_len]
        if prefix in name_dict:
            if name in name_dict[prefix]:
                name_dict[prefix][name] += 1
                print(name + str(name_dict[prefix][name]))
                flag = False
                break
            else:
                flag = True
                for key, value in name_dict[prefix].items():
                    idx = same_part(key, name)
                    q.append(name[:idx+1])
                    continue
        else:
            if not flag:
                name_dict[prefix][name] = 1
                print(prefix)
                break
    if flag:
        val = ''
        while q:
            p = q.popleft()
            if len(val) < len(p):
                val = p
        name_dict[val][name] = 1
        print(val)