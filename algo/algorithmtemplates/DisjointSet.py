# Information taken from Leetcode's Disjoint Set
class DisjointSet:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]

    def find(self, index: int) -> int:
        return self.root[index]

    def union(self, parent: int, child: int) -> None:
        parent_root = self.find(parent)
        child_root = self.find(child)
        if parent_root != child_root:
            for i in range(len(self.root)):
                if self.root[i] == child_root:
                    self.root[i] = parent_root

    def connected(self, parent: int, child: int) -> bool:
        return self.find(parent) == self.find(child)
