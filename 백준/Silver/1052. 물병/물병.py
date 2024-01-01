import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))

count = 0

while str(bin(n)).count('1') > k: # n개의 물병으로 만들 수 있는 최소의 물병 개수로 해야 함 -> 이진수를 이용
    n += 1
    count += 1

print(count)