import sys
input = sys.stdin.readline

chennel = int(input())
num = int(input())
delete_button = list(map(int, input().split())) if num != 0 else []
buttons = [str(i) for i in range(10) if i not in delete_button]

near_num = [abs(chennel - 100), 0]
for i in range(1000001):
    check = 1
    
    for num in str(i):
        if num not in buttons:
            check = 0
            break
    
    buffer = abs(chennel - i)
    if check == 1 and near_num[0] > buffer:
        near_num[0], near_num[1] = buffer, len(str(i))

print(sum(near_num) if sum(near_num) < abs(chennel - 100) else abs(chennel - 100))