import sys
input = sys.stdin.readline

dic = dict()
count = 0
while True:
    name = input().rstrip()
    if not name: break
    if name not in dic.keys():
        dic[name] = 1
    else:
        dic[name] += 1
    count += 1

for i in sorted(dic.keys()):
    print(i, '%.4f' % (dic[i] * 100 / count))