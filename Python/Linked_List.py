class Node:
    def __init__(self, v=None, w=None):
        self.v = v
        self.w = w
        self.next = None


class LinkedList:
    def __init__(self):
        self.__header = None

    def append(self, x, l):
        tmpNode = Node(x, l)
        tmpNode.next = self.__header
        self.__header = tmpNode

    def header(self):
        return self.__header
