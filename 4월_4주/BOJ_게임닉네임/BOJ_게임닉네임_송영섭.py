import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
name_dick = defaultdict(set)
name_num_dick = defaultdict(int)
nick_dict = defaultdict(int)

for _ in range(N):
    name = str(input().rstrip())

    if name in name_dick.keys():
        name_num_dick[name] += 1
        print(name + str(name_num_dick[name] + 1))
    
    else:
        check = 0
        for idx in range(1, len(name)+1):
            name_dick[name].add(name[:idx])
            if name[:idx] not in nick_dict:
                nick_dict[name[:idx]] = 0
                if check == 0:
                    print(name[:idx])
                    check = 1
        else:
            if nick_dict[name] == 0 and check == 0:
                nick_dict[name] == 1
                print(name)