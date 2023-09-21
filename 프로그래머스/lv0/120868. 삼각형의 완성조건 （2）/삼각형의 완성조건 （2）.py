def solution(sides):
    count, sides = 0, sorted(sides)
    for i in range(sides[1]):
        if sides[0] + i > sides[1]: count += 1
    return count + sides[0]