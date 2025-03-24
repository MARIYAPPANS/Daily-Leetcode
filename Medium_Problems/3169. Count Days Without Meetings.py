from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        m = []
        for s, e in meetings:
            if not m or m[-1][1] < s - 1:
                m.append([s, e])
            else:
                m[-1][1] = max(m[-1][1], e)
        busy = sum(e - s + 1 for s, e in m)
        return days - busy
