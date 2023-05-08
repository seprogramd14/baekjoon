def solution(s):
    stack = []
    for w in s:
        if w == ')': stack.pop() if stack else stack.append(w)
        elif w == '(': stack.append(w)
    return bool(not stack)
