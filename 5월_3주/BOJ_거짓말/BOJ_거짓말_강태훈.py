import sys
input = lambda :list(map(int, sys.stdin.readline().split()))

def make_group(arr):
    return sum([1<<i for i in arr[1:]])

def main():
    n, m = map(int, input())
    know_truth = make_group(input())
    party = [make_group(input()) for i in range(m)]

    while True:
        new = know_truth
        for i in party:
            if new&i:
                new|=i
        if new==know_truth:
            break
        know_truth=new
    print(sum([not(i&know_truth) for i in party]))
if __name__=="__main__":
    main()

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