def solution(chicken):
    answer = 0
    coupon = 0 # 10개가 안되는 쿠폰의 개수
    while chicken >= 10:
        answer += (chicken // 10)
        chicken = (chicken % 10) + chicken // 10
        print(chicken)
    return answer