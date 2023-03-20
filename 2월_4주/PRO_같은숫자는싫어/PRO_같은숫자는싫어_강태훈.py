def solution(arr):
    stack = []
    for i in arr:
        stack.append(i)
        while len(stack) >= 2 and stack[-1]==stack[-2]:
            stack.pop()
    return stack