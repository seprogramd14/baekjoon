import sys
input = sys.stdin.readline

M, m = -float('inf'), float('inf')
def recur(opes, i, result = 0):
    global M, m
    if not sum(opes.values()):
        if result < m:
            m = result
        if result > M:
            M = result
        return 
    
    for key in opes.keys():
        if opes[key] != 0:
            opes_c = opes.copy()
            opes_c[key] -= 1
            # key로 연산
            if i == 1:
                res = eval(f'{nums[i-1]} {key} {nums[i]}')
                recur(opes_c, i+1, res)
            else:
                if key == '//' and result < 0:
                    res = -eval(f'{-result} {key} {nums[i]}')
                else:
                    res = eval(f'{result} {key} {nums[i]}')
                recur(opes_c, i+1, res)

n = int(input())
nums = list(map(int, input().split()))
ope_nums = list(map(int, input().split()))
ope = {s:i for s, i in zip('+-*', ope_nums[:-1])}
ope['//'] = ope_nums[-1]
recur(ope, 1)
print(M, m, sep='\n')
