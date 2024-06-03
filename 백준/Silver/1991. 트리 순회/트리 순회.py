import sys
input = sys.stdin.readline
n = int(input())
tree = {}

for i in range(n):
    key, *node = input().split()
    tree[key] = node

r1 = []
def start(root):
    global r1
    if root == ".":
        return

    r1.append(root)
    start(tree[root][0])
    start(tree[root][1])
start('A')

r2 = []
def mid(root):
    global r2
    if root == ".":
        return

    mid(tree[root][0])
    r2.append(root)
    mid(tree[root][1])
mid('A')

r3 = []
def end(root):
    global r3
    if root == ".":
        return

    end(tree[root][0])
    end(tree[root][1])
    r3.append(root)
end('A')

print(''.join(r1))
print(''.join(r2))
print(''.join(r3))