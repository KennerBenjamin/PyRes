import math


class MinHeap:
    def __init__(self):
        self.tree = []

    def insert(self, clause, count, evaluation):
        clause = [evaluation, clause, count]
        self.tree.append(clause)
        self.bubbleup(len(self.tree) - 1)

    def bubbleup(self, node):
        if node == 0:
            return
        parent = math.ceil((node / 2) - 1)
        if self.tree[parent][0] <= self.tree[node][0]:
            return
        else:
            self.switch(node, parent)
            self.bubbleup(parent)

    def getBest(self):
        if not self.tree:
            return None, None, True
        clause = self.tree[0][1]
        count = self.tree[0][2]
        self.tree[0] = self.tree.pop()
        self.bubbledown(0)
        return clause, count, False

    def bubbledown(self, node):
        leftchild = (2 * node) + 1
        if leftchild > (len(self.tree) - 1):
            return
        rightchild = leftchild + 1
        if rightchild > (len(self.tree) -1):
            if self.tree[leftchild][0] < self.tree[node][0]:
                temp = self.tree[leftchild]
                self.tree[leftchild] = self.tree[node]
                self.tree[node] = temp
            return
        if self.tree[leftchild][0] < self.tree[node][0] or self.tree[rightchild][0] < self.tree[node][0]:
            if self.tree[leftchild][0] <= self.tree[rightchild][0]:
                self.switch(node, leftchild)
                self.bubbledown(leftchild)
            else:
                self.switch(node, rightchild)
                self.bubbledown(rightchild)

    def switch(self, node1, node2):
        temp = self.tree[node1]
        self.tree[node1] = self.tree[node2]
        self.tree[node2] = temp


