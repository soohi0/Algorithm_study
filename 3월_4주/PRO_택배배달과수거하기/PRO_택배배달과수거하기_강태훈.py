def solution(cap, n, deliveries, pickups):
    processed_d = processed_p = answer = 0
    
    for idx, (delivery, pickup) in enumerate(zip(deliveries[::-1], pickups[::-1])):
        print("*"*30)
        print(f"현재 {n-idx}번 집 처리중.",)
        print(f"{n-idx}번 집에는 {delivery}개의 배달해야 할 택배상자가 있지만 {-processed_d}개는 이전에 처리 된 상태이므로 {max(delivery+processed_d,0)}개만 처리하면 됨")
        print(f"{n-idx}번 집에는 {pickup}개의 수거해야 할 택배상자가 있지만 {-processed_p}개는 이전에 처리 된 상태이므로 {max(pickup+processed_p,0)}개만 처리하면 됨")
        size = 1+(max(processed_d+delivery, processed_p+pickup)-1)//cap
        print(f"{max(processed_d+delivery, processed_p+pickup)}개를 처리해야 함. cap={cap}이므로 {size}번 왕복을 통해 {n-idx}번 집 처리 완료가 가능")
        processed_d += delivery-size*cap
        processed_p += pickup-size*cap
        answer += size*(n-idx)
        print(f"{n-idx}번 집을 {size}번 왕복")
        print(f"남은 배달 횟수 : {-processed_d}")
        print(f"남은 수거 횟수 : {-processed_p}")
        print(f"{n-idx-1}~1번 집에 있는 {-processed_d}개의 택배상자를 추가로 배달 가능")
        print(f"{n-idx-1}~1번 집에 있는 {-processed_p}개의 택배상자를 추가로 수거 가능")
        print("*"*30)
    return answer*2

"""
answer      : 정답
processed_d : n번 집에 대한 처리가 끝난 시점에서 남은 배달 횟수
processed_p : n번 집에 대한 처리가 끝난 시점에서 남은 수거 횟수
size        : n번 집에 대한 처리가 끝나기 위해 필요한 왕복 횟수
"""
if __name__ == "__main__":
    test_case = [
        [4,	5,	[1, 0, 3, 1, 2],	[0, 3, 0, 4, 0],	16],
        [2,	7,	[1, 0, 2, 0, 1, 0, 2],	[0, 2, 0, 1, 0, 2, 0],	30],
    ]
    for case in test_case:
        print(
            f"result = {solution(*case[:-1])}",
            f"groudtruth = {case[-1]}"
        )
