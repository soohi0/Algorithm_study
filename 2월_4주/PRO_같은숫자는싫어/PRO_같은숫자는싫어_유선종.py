from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = []
    while arr:
        num = arr.popleft()
        answer.append(num)
        while True:
            if arr:
                if arr[0] == num:
                    arr.popleft()
                else:
                    break
            else:
                break
    return answer