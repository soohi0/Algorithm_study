import sys 
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    n = int(input())
    nbook = [input() for _ in range(n)]
    nbook.sort()

    # flag = 0
    # for i, a in enumerate(nbook[:-1]):
    #     for j, b in enumerate(nbook[i+1:]):
    #         if len(a) == len(b):
    #             continue
    #         if a==b[:len(a)]:
    #             print('NO')
    #             flag = 1
    #             break
    #     if flag == 1:
    #         break 
    # if flag == 0:
    #     print('YES')

    # flag = 0
    # for i, b in enumerate(nbook):
    #     temp_book = list(map(lambda x: x[:len(b)], nbook))
    #     if b in temp_book[i+1:]:
    #         print('NO')
    #         flag=1
    #         break
    # if flag == 0:
    #     print('YES')
    
    flag = 0
    for i, b in enumerate(nbook[:-1]):
        if b == nbook[i+1][:len(b)]:
            print('NO')
            flag=1
            break
    if flag == 0:
        print('YES')
    