def solution(binomial):
    a, op, b = binomial.split()
    answer = 0
    if op == "+":
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)