def solution(nums):
    answer = 0
    return min(len(nums)//2, len(set(nums)))