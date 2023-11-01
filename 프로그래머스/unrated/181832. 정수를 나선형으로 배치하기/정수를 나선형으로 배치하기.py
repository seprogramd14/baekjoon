def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n): answer[0][i] = i+1
    count = 1
    start_row = 0
    end_row = n-1
    start_col = 0
    end_col = n-1

    while count <= n*n:
        for i in range(start_col, end_col+1):
            answer[start_row][i] = count
            count += 1
        start_row += 1

        for i in range(start_row, end_row+1):
            answer[i][end_col] = count
            count += 1
        end_col -= 1

        for i in range(end_col, start_col-1, -1):
            answer[end_row][i] = count
            count += 1
            print(i)
        end_row -= 1

        for i in range(end_row, start_row-1, -1):
            answer[i][start_col] = count
            count += 1
        start_col += 1
    return answer