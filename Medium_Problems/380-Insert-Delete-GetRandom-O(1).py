import random

class RandomizedSet:

    def __init__(self):
        self.values = {}
        self.indexes = []
        
    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.values[val] = len(self.indexes)
        self.indexes.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        idx = self.values[val]
        last_val = self.indexes[-1]
        self.indexes[idx] = last_val
        self.values[last_val] = idx
        self.indexes.pop()
        del self.values[val]
        return True
        
    def getRandom(self) -> int:
        return self.indexes[random.randint(0, len(self.indexes) - 1)]
