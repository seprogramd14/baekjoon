def search_room(k, n):
    for i in range(1, k+1):
        for j in range(1, n+1):
            room[i][j-1] = sum(room[i-1][:j])
    return room[k][n-1]

room = [[0] * 14 for _ in range(15)]
for i in range(14):
    room[0][i] = i+1

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(search_room(k, n))