class ProductOfNumbers:
    def __init__(self):
        self.p = [1]

    def add(self, n: int) -> None:
        if n == 0:
            self.p = [1]
        else:
            self.p.append(self.p[-1] * n)

    def getProduct(self, k: int) -> int:
        return 0 if k >= len(self.p) else self.p[-1] // self.p[-(k + 1)]
