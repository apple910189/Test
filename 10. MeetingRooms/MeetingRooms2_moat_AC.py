from typing import List

class MeetingEvent:
    def __init__(self, time: int, is_start: bool):
        self.time = time
        self.is_start = is_start

    def __lt__(self, other):
        # 若時間相同，結束事件排在開始事件前
        if self.time == other.time:
            return not self.is_start
        return self.time < other.time


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        events = []
        # 把每個會議拆成開始 / 結束事件
        for start, end in intervals:
            events.append(MeetingEvent(start, True))
            events.append(MeetingEvent(end, False))
        
        # 依照 __lt__ 排序
        events.sort()
        
        current = 0
        max_rooms = 0
        
        for e in events:
            if e.is_start:
                current += 1
            else:
                current -= 1
            max_rooms = max(max_rooms, current)
        
        return max_rooms


# 🧪 測試
meetings = [
    [0, 30],
    [5, 10],
    [15, 20]
]

sol = Solution()
print(sol.minMeetingRooms(meetings))  # 輸出: 2