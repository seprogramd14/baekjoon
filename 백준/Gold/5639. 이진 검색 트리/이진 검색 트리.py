import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break

def sub_tree(node_list):
    if node_list:
        root = node_list[0]
        if len(node_list) == 1:
            print(root)
            return
        sub_tree([node for node in node_list[1:] if node < root])
        sub_tree([node for node in node_list[1:] if node > root])
        print(root)

sub_tree(nodes)