# 1. 비트마스킹
import sys
input = lambda :map(int, sys.stdin.readline().split())

def make_group(arr, v=0):
    next(arr)
    for i in arr:
        v |= 1<<i
    return v

def main(know_truth, party):
    while True:
        new = know_truth
        for i in party:
            if new&i:
                new|=i
        if new==know_truth:
            break
        know_truth=new
    print(sum(not(i&know_truth) for i in party))

if __name__=="__main__":
    n, m = input()
    know_truth = make_group(input())
    party = [make_group(input()) for i in range(m)]
    main(know_truth, party)

# # 2. 분리집합
# import sys
# input = sys.stdin.readline

# def find(v, parent):
#     if parent[v]!=v:
#         parent[v] = find(parent[v], parent)
#     return parent[v]
    
# def union(v1, v2, parent):
#     p1, p2 = find(v1, parent), find(v2, parent)
#     parent[max(p1, p2)] = parent[min(p1, p2)]

# def main():
#     n, m = map(int, input().split())
#     know_truth = set(list(map(int, input().split()))[1:])
#     parent = [0 if i in know_truth else i for i in range(n+1)]
#     participants = []
#     for _ in range(m):
#         party_info  = list(map(int, input().split()))
#         participants.append(party_info[1:])
#         v1 = party_info[1]
#         for v2 in party_info[2:]:
#             union(v1, v2, parent)
#     cnt = 0
#     for party in participants:
#         if 0 not in set(map(lambda x:find(x, parent), party)):
#             cnt += 1
#     print(cnt)

# if __name__=="__main__":
#     main()