def solution(num_list):
    answer = []
    for num in num_list:
        cnt = 0
        while num != 1:
            if num % 2 == 0: num //= 2
            else: num = (num-1) // 2
            cnt += 1
        answer.append(cnt)
    return sum(answer)