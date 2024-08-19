import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    nums = []
    for _ in range(n // 10 + 1):
        nums += list(map(int, input().split()))

    print(n // 2 + 1)
    left, right = [], []
    med = nums[0]
    result = [nums[0]]
    for i in range(1, n):
        if nums[i] <= med:
            heapq.heappush(left, -nums[i])
        else:
            heapq.heappush(right, nums[i])

        if not i % 2:
            if len(left) > len(right):
                heapq.heappush(right, med)
                med = -heapq.heappop(left)
            elif len(left) < len(right):
                heapq.heappush(left, -med)
                med = heapq.heappop(right)
            result.append(med)

    for i in range(len(result)):
        print(result[i], end=' ')
        if not (i+1) % 10:
            print()
    print()
