import sys
input = sys.stdin.readline

n = int(input())

ls = list(map(int, input().rstrip().split()))
S = list(set(ls))
S.sort()

dic = {S[i]:i for i in range(len(S))}

result = [dic[k] for k in ls]
print(*result)