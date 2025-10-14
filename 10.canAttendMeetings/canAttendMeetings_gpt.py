from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True

s = Solution()

intervals = [[0,30],[5,10],[15,20]]
ans = s.canAttendMeetings(intervals)
print(ans)

intervals2 = [[7,10],[2,4]]
ans2 = s.canAttendMeetings(intervals2)
print(ans2)