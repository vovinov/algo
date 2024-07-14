"""
Give an array of meeting times intervals where intervals[i] = [start, end],
determine if a person could attend all meetings
"""


def CouldAttendMeetings(intervals) -> bool:

    intervals.sort()

    for i in range(1, len(intervals)):

        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


#  print(CouldAttendMeetings([[0, 30], [5, 10], [15, 20]]))
print(CouldAttendMeetings([[7, 10], [2, 4]]))
