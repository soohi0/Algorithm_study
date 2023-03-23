# 효율성에서 3개 시간초과 - 다시 시도해보기 
def solution(people, limit):
    answer = 0
    ppl = sorted(people, reverse=True)
    p1, p2 = 0, len(ppl)-1 # 투포인터
    while p1 < p2:
        per1, per2 = ppl[p1], ppl[p2]
        if per1 + per2 == limit: # 딱 맞는경우
            answer += 1
            ppl.remove(per1) # 시간 오래걸림 . 리스트 원소 자체를 빼는건 조금 지양해야함.
            ppl.remove(per2) 
            p1, p2 = 0, len(ppl)-1 # 초기화
        elif per1 + per2 < limit: # 사람 더넣을 수 있음
            # p2 를 왼쪽으로 당김
            p2 -= 1
            if per1 + ppl[p2] > limit or p1 == p2: 
                # 옮겼는데 초과 혹은 겹침 - 지금것을 뻄
                answer += 1
                ppl.remove(per1)
                ppl.remove(per2)
                p1, p2 = 0, len(ppl)-1
                continue
        elif per1 + per2 > limit: # 초과
            # p1 오른쪽으로
            p1 += 1
            
    answer += len(ppl) # 남은 사람들 다 더해
            
    
    
    
    
    return answer