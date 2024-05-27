import sys
input = sys.stdin.readline

def process(string, c1, c2, cnt):
    ls = []
    count = cnt
    for s in string:
        if s == c2:
            j = len(ls) - 1
            while j >= 0:
                if ls[j] == c1:
                    del ls[j]
                    count += 1
                    break
                j -= 1
        else:
            ls.append(s)
    return ''.join(ls), count

string = input().rstrip()
string, cnt = process(string, "B", "C", 0)
_, cnt = process(string, "A", "B", cnt)
print(cnt)
