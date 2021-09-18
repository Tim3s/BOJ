import sys


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = None if left == '.' else left
        self.right = None if right == '.' else right


def prefix(root):
    print(root.data, end='')
    if root.right:
        prefix(nodeset[root.right])
    if root.right:
        prefix(nodeset[root.right])


def infix(root):
    if root.right:
        infix(nodeset[root.right])
    print(root.data, end='')
    if root.right:
        infix(nodeset[root.right])


def postfix(root):
    if root.right:
        postfix(nodeset[root.right])
    if root.right:
        postfix(nodeset[root.right])
    print(root.data, end='')


nodeset = dict()
notparent = set()
N = int(sys.stdin.readline())
for i in range(N):
    tmp = sys.stdin.readline().split()
    nodeset[tmp[0]] = Node(tmp[0], tmp[1], tmp[2])
    if tmp[1] != '.':
        notparent.add(tmp[1])
    if tmp[2] != '.':
        notparent.add(tmp[2])
for key in nodeset:
    if nodeset[key] not in notparent:
        parent = nodeset[key]
        break
prefix(parent)
print()
infix(parent)
print()
postfix(parent)
