def solution(number, k):
    answer = number[0]
    for s in number[1:]:
        while len(answer) > 0 and int(answer[-1]) < int(s) and k > 0:
            answer = answer[:-1]
            k-=1
        answer += s
        
    if k > 0:
        answer = answer[:-k]
    return answer