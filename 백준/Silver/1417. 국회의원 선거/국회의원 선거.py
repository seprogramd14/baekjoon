n = int(input())
person = [int(input()) for _ in range(n)]
cnt = 0
if len(person) > 1:
    p, er = person[0], person[1:]
    while p <= max(er):
        i = er.index(max(er))
        p, er[i] = p+1, er[i]-1
        cnt += 1
print(cnt)