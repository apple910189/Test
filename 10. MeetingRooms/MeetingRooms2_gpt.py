from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 分開所有開始和結束時間
        starts = sorted([i[0] for i in intervals])
        ends   = sorted([i[1] for i in intervals])
        
        rooms = 0
        max_rooms = 0
        i = j = 0
        
        # 用雙指標走訪
        while i < len(intervals):
            if starts[i] < ends[j]:
                # 新會議開始，房間數 +1
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                # 有會議結束，房間數 -1
                rooms -= 1
                j += 1
        
        return max_rooms


s = Solution()

intervals = [[0,30],[5,10],[15,20]]
ans = s.minMeetingRooms(intervals)
print(ans)

intervals2 = [[7,10],[2,4]]
ans2 = s.minMeetingRooms(intervals2)
print(ans2)

intervals3 = [[4,9],[4,17],[9,10]]
ans3 = s.minMeetingRooms(intervals3)
print(ans3)