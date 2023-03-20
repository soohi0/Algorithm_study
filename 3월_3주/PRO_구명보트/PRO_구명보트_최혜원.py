def solution(people, limit):
    answer = 0
    
    sorted_people = sorted(people)
    print(sorted_people)
    part_sum = 0
    for idx, weight in enumerate(sorted_people):
        # print(part_sum, weight, answer)
        if part_sum + weight <= limit:
            part_sum += weight
            if idx < len(sorted_people)-1:
                if sorted_people[idx+1] + part_sum > limit:
                    part_sum = 0
                    answer += 1
            elif idx == len(sorted_people)-1:
                answer += 1
    
    return answer