# 11:00
# 한 번호가 다른번호로 시작하면 안됨.
# 일단 짧은번호부터 시작
from collections import defaultdict
import heapq
import sys
input = lambda : sys.stdin.readline().strip()

def check(book, seq):
    # 하나씩 돌아가면서 startswith를 판단한다.
    while seq:
        l, number = heapq.heappop(seq)
        for i in range(l+1, 11):
            if book[i]:
                for bnum in book[i]:
                    if bnum.startswith(number):
                        return 'NO'
    return 'YES'  

t = int(input())
for _ in range(t):
    n = int(input())
    book = defaultdict(list)
    seq = []
    for _ in range(n):
        num = input()
        book[len(num)].append(num)
        heapq.heappush(seq, (len(num), num))
    print(check(book, seq))


# 짧은값부터 조회해서 해시에 넣음 
'''
(자리수, 숫자, 순번)로 집어넣기
1,9 : 3 / 2,1 : 2, / 2,7 : 1 / 3,1 : 2 / 3,6: 1
'''