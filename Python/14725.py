import sys


class Trie:
    def __init__(self):
        self.__child = dict()
        self.__childs = []

    def append(self, childs):
        if childs:
            if childs[0] not in self.__child:
                self.__child[childs[0]] = Trie()
                self.__childs.append(childs[0])
            self.__child[childs[0]].append(childs[1:])

    def print(self, prefix):
        self.__childs.sort()
        for child in self.__childs:
            print(prefix + child)
            self.__child[child].print(prefix + '--')


N = int(sys.stdin.readline())
root = Trie()
for _ in range(N):
    root.append(sys.stdin.readline().split()[1:])
root.print('')
