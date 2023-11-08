import sys
input = sys.stdin.readline

N, r, c = list(map(int, input().split()))
count = 0

while N != 0:
    N -= 1
    # 1번 구역
    if r < 2**N and c < 2**N:
        count += (2**N) ** 2 * 0
    # 2번 구역
    elif r < 2**N and c >= 2**N:
        count += (2**N) ** 2 * 1
        c -= (2**N)
    # 3번 구역
    elif r >= 2**N and c < 2**N:
        count += (2**N) ** 2 * 2
        r -= (2**N)
    # 4번 구역
    elif r >= 2**N and c >= 2**N:
        count += (2**N) ** 2 * 3
        r -= (2**N)
        c -= (2**N)

print(count)