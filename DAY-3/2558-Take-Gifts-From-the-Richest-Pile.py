class Solution(object):
    def pickGifts(self, gifts, k):
        import math
        for i in range(k):
            max_index = gifts.index(max(gifts))
            gifts[max_index] = int(math.sqrt(gifts[max_index]))
        return sum(gifts)
