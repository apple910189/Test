class MeetingInterval:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


class MeetingEvent:
    def __init__(self, time, is_start_meeting):
        self.time = time
        self.is_start_meeting = is_start_meeting

    def __lt__(self, other):
        if self.time == other.time:
            if self.is_start_meeting != other.is_start_meeting:
                return !self.is_start_meeting
            else:
                return False
        return self.time < other.time


class Solution:
    def minimum_meeting_room(self, meetings):
        events = []
        for meeting in meetings:
            events.append(MeetingEvent(meeting.start_time, True))
            events.append(MeetingEvent(meeting.end_time, False))

        events.sort()

        maximum_meeting_room_needed = 0
        current_meeting = 0

        for event in events:
            if event.is_start_meeting:
                current_meeting += 1
            else:
                current_meeting -= 1
            maximum_meeting_room_needed = max(current_meeting, maximum_meeting_room_needed)

        return maximum_meeting_room_needed