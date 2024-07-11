"""
You are given a string s.
The record only contains the following three characters:
'A': Absent. 'L': Late. 'P': Present.
The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award,
or false otherwise.
"""


def checkRecord(s: str):

    count_l = 0

    if s.count("A") > 1:
        return False

    for grade in s:

        if grade == "L":
            count_l += 1
        else:
            count_l = 0

        if count_l > 2:
            return False

    return True


print(checkRecord("PPALLP"))
print(checkRecord("PPALLL"))
