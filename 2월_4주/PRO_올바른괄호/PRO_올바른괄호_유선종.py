def solution(s):
    q = []
    for i, bracket in enumerate(s):
        if q:
            if q[-1] == '(':
                if bracket == ')':
                    q.pop()
                else:
                    if i == len(s)-1:
                        return False
                    else:
                        q.append('(')
            else:
                return False
        else:
            if bracket == '(':
                q.append('(')
            else:
                return False

    return False if q else True