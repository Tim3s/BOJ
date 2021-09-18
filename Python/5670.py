import sys


class Trie:
    def __init__(self):
        self.__child = dict()
        self.__done = False

    def append(self, childs):
        if childs:
            if childs[0] not in self.__child:
                self.__child[childs[0]] = Trie()
            self.__child[childs[0]].append(childs[1:])
        else:
            self.__done = True

    def print(self, cnt):
        if cnt:
            res = cnt if self.__done else 0
            if len(self.__child) == 0:
                return res
            elif len(self.__child) == 1:
                for key in self.__child:
                    return res + self.__child[key].print(cnt + (1 if res else 0))
            cnt += 1
            for key in self.__child:
                res += self.__child[key].print(cnt)
            return res
        else:
            res = 0
            for key in self.__child:
                res += self.__child[key].print(1)
            return res


while True:
    try:
        N = int(sys.stdin.readline())
    except:
        break
    root = Trie()
    for _ in range(N):
        root.append(list(sys.stdin.readline().rstrip()))
    print(format(root.print(0) / N, '.2f'))
