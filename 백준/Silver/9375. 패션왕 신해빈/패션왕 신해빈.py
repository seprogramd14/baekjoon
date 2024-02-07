import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    num = int(input())
    clothes = dict()
    for i in range(num):
        cloth, part = list(map(str, input().rstrip().split()))
        if part in clothes.keys():
            clothes[part] += 1
        else:
            clothes[part] = 1
    result = 1 # 조합식 잘 생각해 보세요
    for c in clothes:
        result *= (clothes[c] + 1)
    print(result - 1)