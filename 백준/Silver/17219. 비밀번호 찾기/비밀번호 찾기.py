import sys
input = sys.stdin.readline

n, m = list(map(int, input().rstrip().split()))
record = dict()

for _ in range(n):
    site, password = list(map(str, input().rstrip().split()))
    record[site] = password

for _ in range(m):
    check = input().rstrip()
    print(record[check])