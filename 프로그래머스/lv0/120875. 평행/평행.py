def solution(dots):
    dots = sorted(dots, key=lambda x : (x[0], x[1]))
    g1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    g2 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    print(g1, g2)
    return 1 if g1 == g2 else 0