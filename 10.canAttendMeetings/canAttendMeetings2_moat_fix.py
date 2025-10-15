class MeetingInterval:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


class MeetingEvent:
    def __init__(self, time, is_start_meeting):
        self.time = time
        self.is_start_meeting = is_start_meeting

    # 定義自訂排序邏輯
    def __lt__(self, other):
        # 若時間相同：結束事件要排在開始事件前
        if self.time == other.time:
            if self.is_start_meeting != other.is_start_meeting:
                return not self.is_start_meeting
            else:
                return False
        # 否則依時間早晚排序
        return self.time < other.time


class Solution:
    def minimum_meeting_room(self, meetings):
        events = []
        for meeting in meetings:
            events.append(MeetingEvent(meeting.start_time, True))   # 開始事件
            events.append(MeetingEvent(meeting.end_time, False))     # 結束事件

        # 依自訂規則排序
        events.sort()

        maximum_meeting_room_needed = 0
        current_meeting = 0

        # 掃描線
        for event in events:
            if event.is_start_meeting:
                current_meeting += 1
            else:
                current_meeting -= 1
            maximum_meeting_room_needed = max(maximum_meeting_room_needed, current_meeting)

        return maximum_meeting_room_needed


# 🧪 測試
meetings = [
    MeetingInterval(0, 30),
    MeetingInterval(5, 10),
    MeetingInterval(15, 20)
]

sol = Solution()
print(sol.minimum_meeting_room(meetings))  # 輸出: 2
