def solution(s):
    stack = 0
    for token in s:
        if token == "(":
            stack += 1
        elif not stack:
            return False
        else:
            stack -= 1
    return False if stack else True