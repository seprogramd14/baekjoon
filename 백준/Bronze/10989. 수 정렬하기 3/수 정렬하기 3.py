import sys
input = sys.stdin.readline
sort_list = [0] * 10001

n = int(input())
for i in range(n):
    sort_list[int(input())] += 1

for i in range(len(sort_list)):
    if sort_list[i] != 0:
        for j in range(sort_list[i]):
            print(i)