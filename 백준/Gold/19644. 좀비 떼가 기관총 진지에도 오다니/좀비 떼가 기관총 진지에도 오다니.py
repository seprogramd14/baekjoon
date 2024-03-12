import sys
input = sys.stdin.readline

l = int(input())
ml, mk = list(map(int, input().split()))
ca = int(input())
zombies = [0] + [int(input()) for _ in range(l)]

shot = [0]

for i in range(1, l+1):
    m = max(0, i-ml)
    d = shot[i-1] - shot[m]
    if zombies[i] <= d + mk:
        shot.append(shot[i-1] + mk)
    else:
        if not ca: # 크레모어 없으면 망
            print('NO')
            exit()
        else:
            ca -= 1
            shot.append(shot[i-1])
print('YES')