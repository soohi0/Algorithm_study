import sys
iput = lambda : sys.stdin.readline().strip()

N = int(input())
nicks = dict()
full_nicks = dict()
for _ in range(N):
    name = list(input())
    temp = ''
    prefix = []
    for n in name:
        temp += n
        if temp not in nicks.keys():
            prefix.append(temp)
        nicks[temp] = 1
    full_nicks[temp] = full_nicks.get(temp,0) + 1
    if len(prefix)==0:
        if full_nicks[temp] > 1:
            prefix.append(temp+str(full_nicks[temp]))
        else:
            prefix.append(temp)
    print(prefix[0])