def solution(numbers, k):
    answer = 0
    for _ in range(k-1):
        answer += 2
        if answer > len(numbers)-1: answer -= len(numbers)
    return numbers[answer]