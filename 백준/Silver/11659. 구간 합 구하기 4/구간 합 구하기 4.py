import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
num = list(map(int, input().split()))

hap = [num[0]]
for i in range(1, len(num)):
    hap.append(hap[i-1]+num[i])
hap = [0] + hap

for _ in range(m): 
    i, j = list(map(int, input().split()))
    print(hap[j] - hap[i-1])