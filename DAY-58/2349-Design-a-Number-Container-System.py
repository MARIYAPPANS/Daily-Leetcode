from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):
        self.idx_num = {}  # Maps index to number
        self.num_idx = defaultdict(list)  # Maps number to a min-heap of indices

    def change(self, i: int, n: int) -> None:
        self.idx_num[i] = n
        heapq.heappush(self.num_idx[n], i)

    def find(self, n: int) -> int:
        while self.num_idx[n]:
            if self.idx_num.get(self.num_idx[n][0]) == n:
                return self.num_idx[n][0]
            heapq.heappop(self.num_idx[n])
        return -1
