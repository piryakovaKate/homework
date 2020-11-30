import random
class BinTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"

    def dfs(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinTree(value)
                else:
                    self.left.dfs(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinTree(value)
                else:
                    self.right.dfs(value)
        else:
            self.value = value

    def __iter__(self):
        if self.left:
            for i in self.left:
                yield i
        yield self
        if self.right:
            for i in self.right:
                yield i


arr = BinTree(40)
for i in range(10):
    arr.dfs(random.randint(1,100))

res = iter(arr)
for i in range(10):
    print(next(res))


