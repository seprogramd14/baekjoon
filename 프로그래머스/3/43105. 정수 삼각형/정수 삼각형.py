def solution(tri):
    a = [[0 for _ in range(len(tri[i]))] for i in range(len(tri))]
    a[0][0] = tri[0][0]
    for i in range(len(tri)-1):
        for j in range(len(tri[i])):
            bu = tri[i+1][j] + a[i][j]
            bu2 = tri[i+1][j+1] + a[i][j]
            if a[i+1][j] != 0: a[i+1][j] = max([a[i+1][j], bu])
            else: a[i+1][j] = bu
            
            if a[i+1][j+1] != 0: a[i+1][j+1] = max([[i+1][j+1], bu2])
            else: a[i+1][j+1] = bu2
    return max(a[-1])