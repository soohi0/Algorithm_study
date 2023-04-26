# #중복 순열 product
# from itertools import product
# def cal_emoticon_pay(discount, price):
#     return int(price * (100 - discount) * 0.01)
    
# def solution(users, emoticons):
#     answer = []
#     results = []
#     discounts = [10, 20, 30, 40]
#     for p in product(discounts, repeat=len(emoticons)):
#         result = [0, 0]
#         for user in users:
#             # print('user:', user)
#             buy_amount = 0
#             for p_idx, discount in enumerate(p):
#                 # print('할인율: ',discount)
#                 if user[0] > discount:
#                     pass
#                 else:
#                     buy_amount += cal_emoticon_pay(discount, emoticons[p_idx])
#                     # print('buy_amount: ',buy_amount)
#             if buy_amount >= user[1]:
#                 result[0] += 1
#             else:
#                 result[1] += buy_amount
#         results.append(result)
#     results.sort(reverse = True)
#     # print(results)
#     answer = results[0]
        
    
#     return answer
def cal_pay(emoticons, halinyul, user):
    u_discount, u_std_pay= user
    all_pay = 0
    e_plus = False
    for idx, e in enumerate(emoticons):
        if halinyul[idx] >= u_discount:
            all_pay += (e * (100-halinyul[idx]) / 100)
    if all_pay >= u_std_pay:
        e_plus = True
        all_pay = 0
    
    return e_plus, all_pay

from heapq import heappush, heappop
from itertools import product
def solution(users, emoticons):
    percentages = [10, 20, 30, 40]
    hq = []
    for p in product(percentages, repeat=len(emoticons)):
        e_plus_cnt = 0
        all_payments = 0
        for user in users:
            e_plus, payments = cal_pay(emoticons, p, user)
            if e_plus:
                e_plus_cnt += 1
            else:
                all_payments += payments
        heappush(hq, [-e_plus_cnt, -all_payments])
    answer = heappop(hq)
    return [-a for a in answer]
    
    #여기서 hq를 사용하게 되면 insert만 계속 하게 되므로 O(nlogn)
    #그냥 값을 변환시켜 최대값을 찾는 시간복잡도인 O(n) 보다 복잡도가 커지므로 
    # heapq 보단느 그냥 값을 갱신시키는 것이 시간이 훨씬 효율적일 것이다.