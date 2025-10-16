from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])  # 參數key是一個函數，而lamda是匿名函數，lamda 輸入: 輸出
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

'''
1️⃣ Meeting Rooms I (LeetCode 252)

題目核心：

給你一些會議時間區間，問你能否全部參加（沒有重疊）。

知識點 / 演算法：

1. 排序 (Sorting)

    先依會議開始時間排序，方便比較相鄰會議。

    intervals.sort(key=lambda x: x[0])

2. 線性掃描 (Linear Scan / Adjacent Comparison)

    只要檢查每個會議與前一個會議的結束時間是否重疊。

    if intervals[i][1] > intervals[i+1][0]: return False

3. 時間複雜度

    排序 O(n log n) + 線性掃描 O(n) → 整體 O(n log n)

核心思想：

    重疊判斷只需要比較相鄰兩個會議，不需要累計同時進行的會議數。
'''