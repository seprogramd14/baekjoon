import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
pre_num = [0]
for i in p:
    pre_num.append(i + pre_num[-1])

m1 = 0
for i in range(1, n): # 벌 - 벌 - 통
    res = 2*pre_num[-1] - p[0] - p[i] - pre_num[i+1]
    if res > m1:
        m1 = res

m2 = 0
for i in range(1, n-1): # 벌 - 통 - 벌
    res = pre_num[i+1] - p[0] + pre_num[-2] - pre_num[i]
    if res > m2:
        m2 = res

m3 = 0
for i in range(n-1): # 통 - 벌 - 벌
    res = pre_num[-2] - p[i] + pre_num[i]
    if res > m3:
        m3 = res

print(max([m1, m2, m3]))