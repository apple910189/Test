class MeetingInterval:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

class Solution:
    def meeting_not_conflict(self, meetings):
        meetings.sort(key=lambda m: m.start_time)
        
        last_meeting_end = meetings[0].start_time
        for i in range(len(meetings)):
            if meetings[i].start_time < last_meeting_end:
                return False
            last_meeting_end = meetings[i].end_time
        return True