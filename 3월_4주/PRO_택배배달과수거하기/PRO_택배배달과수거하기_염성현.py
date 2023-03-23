# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     dsum = 0
#     psum = 0
#     dterm = []
#     pterm = []
#     while sum(deliveries)+sum(pickups) > 0:
#         dsum = 0
#         dab = []
#         while len(deliveries) >0 and dsum <cap:
#             a = len(deliveries)
#             d = deliveries.pop()
#             if d == 0:
#                 continue
#             dab.append(a)
#             dsum += d
#         deliveries.append(dsum-cap)
#         dterm.append(dab)
        
#         psum = 0
#         pab = []
#         while len(pickups)>0 and psum <cap:
#             a = len(pickups)
#             p = pickups.pop()
#             if p == 0:
#                 continue
#             pab.append(a)
#             psum += p
#         pickups.append(psum-cap)
#         pterm.append(pab)
#     for i in range(max(len(dterm),len(pterm))):
#         if dterm[i][0] >= pterm[i][0]:
#             answer += 2*dterm[i][0]
#         else:
#             answer += 2*pterm[i][0]
#     return answer

def solution(cap, n, deliveries, pickups):
    processed_d = processed_p = answer = 0 

    for idx, (delivery, pickup) in enumerate(zip(deliveries[::-1],pickups[::-1])):
        size = 1+(max(processed_d+delivery, processed_p+pickup)-1)//cap
        processed_d += delivery-size*cap
        processed_p += pickup-size*cap
        answer += size*(n-idx)
    return answer*2

def solution(cap, n, deliveries, pickups):
    idx = n-1
    total_distance = 0

    while idx >=0:
        d_sum, p_sum = 0, 0
        while idx>=0 and not deliveries[idx] and not pickups[idx]:
            idx-=1
        
        distance = (idx+1)*2
        total_distance+=distance
        
        while idx >=0 and d_sum+deliveries[idx] <= cap and p_sum + pickups[idx] <= cap:
            d_sum += deliveries[idx]
            p_sum += pickups[idx]
            idx -=1
        
        deliveries[idx] -= (cap - d_sum)
        pickups[idx] -= (cap - p_sum)
        
    return total_distance