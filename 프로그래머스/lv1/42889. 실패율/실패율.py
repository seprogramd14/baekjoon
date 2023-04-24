def solution(N, stages):
    cut = len(stages)
    count = []
    answer = []
    for i in range(1, N+1):
        try:
            val = stages.count(i)/cut
            count.append((i, val))
            cut -= stages.count(i)
        except:
            count.append((i, 0))
    count.sort(key = lambda x : (x[1], -x[0]), reverse=True)
    for i, val in count: answer.append(i)
    return answer