def solution(order):
    answer = 0
    coffee = {"americano":4500, "cafelatte":5000, "anything":4500}
    for i in order:
        i = i.replace('ice', '').replace('hot', '')
        answer += coffee[i]
    return answer