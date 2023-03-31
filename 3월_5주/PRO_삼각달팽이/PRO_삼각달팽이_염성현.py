
def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                x += 1
            elif i% 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            num+=1
    return sum(answer,[])

# def solution(n):
#     answer = []
#     graph = [[0]*(i+1) for i in range(n)]
#     c = 1
#     k = 0
#     h = 0
#     while c < sum(range(n+1))+1:    
#         i = 0 + k
#         j = 0 + k
#         if i!=0 and j!=0:
#             i +=1
#         while i < n -k:
#             if c > sum(range(n+1)):
#                 break
#             graph[i][j] = c
#             i+=1
#             c+=1
#         i-=1
#         j+=1
#         if k!=0:
#             h = 1
#         while j < n -k -h:
#             if c > sum(range(n+1)):
#                 break
#             graph[i][j] = c
#             j+=1
#             c+=1
#         j-=1
#         i-=1
#         j-=1
#         while j > k-h and i > k:
#             if c > sum(range(n+1)):
#                 break
#             graph[i][j] = c
#             i-=1
#             j-=1
#             c+=1
#         k +=1
#     for g in graph:
#         answer += g
#     return answer
