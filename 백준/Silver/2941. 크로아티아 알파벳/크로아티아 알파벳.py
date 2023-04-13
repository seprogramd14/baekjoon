string = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = []
cut = 0
for i in croa: # 개수 세기
    cut += string.count(i)
print(len(string) - cut)