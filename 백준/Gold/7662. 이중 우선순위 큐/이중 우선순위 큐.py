import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    min_heap = []
    max_heap = []
    sync = dict()
    for _ in range(int(input())):
        op, num = input().split()
        num = int(num)
        if op == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num in sync.keys():
                sync[num] += 1
            else:
                sync[num] = 1

        elif op == "D":
            if num == -1 and min_heap: # 최솟값 삭-제
                check = heapq.heappop(min_heap)
                while min_heap and sync[check] <= 0:
                    check = heapq.heappop(min_heap)
                if sync[check] > 0:
                    sync[check] -= 1
            elif num == 1 and max_heap: # 최댓값 삭-제
                check = -heapq.heappop(max_heap)
                while max_heap and not sync[check]:
                    check = -heapq.heappop(max_heap)
                if sync[check] > 0:
                    sync[check] -= 1
    
    result = [k for k, v in sync.items() if v > 0]
    if result:
        print(max(result), min(result))
    else:
        print("EMPTY")
