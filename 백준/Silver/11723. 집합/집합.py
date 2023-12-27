# 집합 연산
# add -> 요소 추가 O(1)
# in, not in -> 요소 확인 O(1)
# remove, discard -> 요소 삭제 O(1)
# clear (set()) -> 공집합 O(1)

import sys
input = sys.stdin.readline

n = int(input())
P = set()

for _ in range(n):
    c = input().split()

    if c[0] == "all":
        P = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
    elif c[0] == "empty":
        P.clear()
    elif c[0] == "add":
        P.add(c[1])
    elif c[0] == "remove":
        P.discard(c[1])
    elif c[0] == "toggle":
        if c[1] in P:
            P.discard(c[1])
        else:
            P.add(c[1])
    elif c[0] == "check":
        if c[1] in P:
            print(1)
        else:
            print(0)