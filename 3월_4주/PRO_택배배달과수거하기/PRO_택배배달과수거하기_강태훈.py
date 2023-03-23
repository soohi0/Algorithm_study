def solution(cap, n, deliveries, pickups):
    processed_d = processed_p = answer = 0
    
    for idx, (delivery, pickup) in enumerate(zip(deliveries[::-1], pickups[::-1])):
        size = 1+(max(processed_d+delivery, processed_p+pickup)-1)//cap
        processed_d += delivery-size*cap
        processed_p += pickup-size*cap
        answer += size*(n-idx)
    return answer*2
