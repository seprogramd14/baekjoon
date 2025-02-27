import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    grade = sorted([list(map(int, input().split())) for _ in range(n)])
    cnt, in_grade = 1, grade[0][1]
    for i in range(1, n):
        if grade[i][1] < in_grade:
            in_grade = grade[i][1]
            cnt += 1
    print(cnt)