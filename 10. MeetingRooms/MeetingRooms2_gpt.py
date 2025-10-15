from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 分開所有開始和結束時間
        starts = sorted([i[0] for i in intervals])
        ends   = sorted([i[1] for i in intervals])
        print(starts,ends)
        rooms = 0
        max_rooms = 0
        i = j = 0
        
        # 用雙指標走訪
        while i < len(intervals):
            print(f'i:{i} j:{j} ',end='')
            if starts[i] < ends[j]:
                # 新會議開始，房間數 +1
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                # 有會議結束，房間數 -1
                rooms -= 1
                j += 1
            print(f'rooms:{rooms} max:{max_rooms}')
        
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

'''
[ [0,30], [5,10], [15,20] ]
(0, start), (5, start), (10, end), (15, start), (20, end), (30, end)
用一個變數 rooms = 0 記當前重疊會議數：
遇到 start → rooms += 1
遇到 end → rooms -= 1
掃描過程中記錄 max_rooms → 這就是最少會議室數量。
'''


'''
2️⃣ Meeting Rooms II (LeetCode 253)

題目核心：
給你一些會議時間區間，問最少需要幾間會議室（也就是最大同時重疊的會議數）。

知識點 / 演算法：
1. 掃描線 (Sweep Line / Event-based Counting)
    每個會議拆成兩個事件：
    開始事件 +1
    結束事件 -1

    按時間排序後掃描，累加 current += 1/-1
    max(current) 就是最少會議室數

2. 自訂排序 / 事件順序
    同一時間點，先處理結束事件再處理開始事件
    保證不會多算房間數
    Python: 自訂 __lt__ 或用 tuple (time, type) 排序

3. 差分概念 (Difference / Delta Array)
    把每個區間的變化拆成 +1 / -1
    用累加求最大值 → 類似「prefix sum 思路」
    但本質是事件累計，不是區間總和

4. 資料結構選擇
    若時間點範圍很大，用 dict 或 list of events，不能直接用陣列
    排序後掃描 → O(n log n)

核心思想：
    找出某一時間點最多同時進行的會議數，就是最少會議室數。
    與 252 不同，需要累計全局重疊，而不是只看相鄰兩個會議。
'''