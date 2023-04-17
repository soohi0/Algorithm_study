def ispossible(mid, k, stones):
    cnt = 0
    for s in stones:
        if s <= mid:
            cnt += 1
            if cnt == k:
                return True
        else:
            cnt = 0
    return False
                
def solution(stones, k):
    answer = 0
    #연속되는 k개 만큼의 숫자에서 가장 큰 숫자를 리턴함.
    # answer 숫자들 중 target 이 되는 숫자가 연속되는 k개 중 가장 큰 숫자를 리턴한다.
    # o(N)이나 O(nlogn)으로 해결하면 될것. 원소 최대값이 200,000,000이니까 이분탐색할 생각하기
    s, e = 1, 200000000
    while s <= e:
        mid = (s+e) // 2
        if ispossible(mid, k, stones):
            e = mid-1
        else:
            s = mid+1
    return s