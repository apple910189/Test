# interval_two_pointers_practice.py
# =======================================
# 雙指標 / 掃描線 類型題目練習筆記
# 作者: Gautam Zianani
# 說明: 每題都展示題意摘要、核心思路與Python骨架。
# =======================================

# ------------------------------------------------------------
# 1️⃣ LeetCode 56 - Merge Intervals
# 題意: 給一堆區間，合併所有重疊的部分。
# 思路: 先依開始時間排序，用一個結果列表維護當前合併區間。
# ------------------------------------------------------------
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])
    return res


# ------------------------------------------------------------
# 2️⃣ LeetCode 986 - Interval List Intersections
# 題意: 給兩個區間列表，找出它們的交集。
# 思路: 兩指標 i, j 各走一個列表，比較重疊部分。
# ------------------------------------------------------------
def intervalIntersection(A, B):
    i, j = 0, 0
    res = []
    while i < len(A) and j < len(B):
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])
        if start <= end:
            res.append([start, end])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return res


# ------------------------------------------------------------
# 3️⃣ LeetCode 253 - Meeting Rooms II
# 題意: 給一堆會議的開始與結束時間，求最少需要多少間房間。
# 思路: 分別排序開始與結束時間，雙指標掃描。
# ------------------------------------------------------------
def minMeetingRooms(intervals):
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    i = j = 0
    rooms = max_rooms = 0
    while i < len(intervals):
        if starts[i] < ends[j]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            i += 1
        else:
            rooms -= 1
            j += 1
    return max_rooms


# ------------------------------------------------------------
# 4️⃣ LeetCode 1094 - Car Pooling
# 題意: 給一堆乘客的上下車地點與人數，檢查車輛是否能容納。
# 思路: 把上車記為 +num，下車記為 -num，依地點排序掃描。
# ------------------------------------------------------------
def carPooling(trips, capacity):
    events = []
    for num, start, end in trips:
        events.append((start, num))
        events.append((end, -num))
    events.sort()
    count = 0
    for _, diff in events:
        count += diff
        if count > capacity:
            return False
    return True


# ------------------------------------------------------------
# 5️⃣ LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
# 題意: 將重疊區間分組，使同組內區間不重疊，求最少組數。
# 思路: 與Meeting Rooms II相同，算最大同時進行數。
# ------------------------------------------------------------
def minGroups(intervals):
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    i = j = 0
    groups = max_groups = 0
    while i < len(intervals):
        if starts[i] <= ends[j]:
            groups += 1
            max_groups = max(max_groups, groups)
            i += 1
        else:
            groups -= 1
            j += 1
    return max_groups


# ------------------------------------------------------------
# 6️⃣ LeetCode 1229 - Meeting Scheduler
# 題意: 給兩人的空閒時段與會議時間，找最早可開會時間。
# 思路: 兩指標比較兩人區間交集。
# ------------------------------------------------------------
def minAvailableDuration(slots1, slots2, duration):
    slots1.sort()
    slots2.sort()
    i = j = 0
    while i < len(slots1) and j < len(slots2):
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])
        if end - start >= duration:
            return [start, start + duration]
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1
    return []


# ------------------------------------------------------------
# 7️⃣ LeetCode 759 - Employee Free Time
# 題意: 多員工的工作時間表，求所有員工的共同空閒時間。
# 思路: 扁平化所有區間，排序後找出間隙。
# ------------------------------------------------------------
def employeeFreeTime(schedule):
    intervals = sorted([iv for emp in schedule for iv in emp])
    res = []
    end = intervals[0][1]
    for s, e in intervals[1:]:
        if s > end:
            res.append([end, s])
        end = max(end, e)
    return res


# ------------------------------------------------------------
# 8️⃣ LeetCode 1272 - Remove Interval
# 題意: 給定區間列表與一個要刪除的區間，輸出刪除後的結果。
# 思路: 比較每個區間與刪除區間的重疊部分，切分或保留。
# ------------------------------------------------------------
def removeInterval(intervals, toBeRemoved):
    res = []
    for s, e in intervals:
        if e <= toBeRemoved[0] or s >= toBeRemoved[1]:
            res.append([s, e])
        else:
            if s < toBeRemoved[0]:
                res.append([s, toBeRemoved[0]])
            if e > toBeRemoved[1]:
                res.append([toBeRemoved[1], e])
    return res


# ------------------------------------------------------------
# ✅ 建議練習順序: [56] → [986] → [253] → [1094] → [2406] → [1229] → [759] → [1272]
# ------------------------------------------------------------

if __name__ == "__main__":
    print("✅ Interval Two Pointers Practice File Loaded!")
    print("建議你可以逐題填寫完整測試用例並運行檢查結果。")
