import heapq

def solution(scoville, K):
    scoville.sort()
    answer = 0
    while (first:=heapq.heappop(scoville)) < K:
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        answer += 1
    return answer