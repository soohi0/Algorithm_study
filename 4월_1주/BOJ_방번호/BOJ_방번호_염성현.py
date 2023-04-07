import sys
input = lambda : sys.stdin.readline().strip()

N = input()

answer = '-1'
for i in range(1, 87655):
    j = int(N)-i
    if j <= 0:
        continue
    if len(list(str(i))+(list(str(j)))) != \
        len(set(str(i))|set(str(j))):
        continue
    answer = str(i) + ' + ' + str(j)
print(answer)

# m : 쌓인 숫자, v : 방문 체크
# def dfs(m, v):
#     global answer
#     flag =0
#     if len(N) <= len(m) < len(N)*2+1:
#         r1,r2 = m[:len(N)], m[len(N):]
#         q1,q2 = m[:len(N)-1],m[len(N)-1:]
#         if len(r1) >0 and len(r2) >0 :
#             if int(r1)+int(r2) == int(N):
#                 answer = r1 + ' + ' + r2 
#                 print(answer)
#                 return
#         if len(q1) >0 and len(q2) >0 :
#             if int(q1)+int(q2) == int(N):
#                 answer = q1 + ' + ' + q2 
#                 print(answer)
#                 return 
        
#     for x in range(1,10):
#         if not v[x]:
#             nm = m+str(x)
#             v[x] = True
#             dfs(nm, v)
#             v[x] = False
# 
# visited= [False]*10
# answer = '-1'
# dfs('',visited)
# print(answer)